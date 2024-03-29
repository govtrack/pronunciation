import unicodedata
import urllib.request
import re
import rtyaml
from collections import defaultdict

with open("legislators.yaml") as f:
	guide = rtyaml.load(f)

def error(msg):
	print(msg)

def parse_symbols(string, symbols, source):
	# Parse the string into a list of symbols. Since some symbols
	# are prefixes of other symbols, assume symbols is sorted in
	# reverse length order and return the longest matching symbol.

	# check that string is already NFC normalized
	if string != unicodedata.normalize("NFC", string):
		error("{} is not Unicode NFC-normalized.".format(string))
		return

	# and has no leading/trailing spaces
	if string != string.strip():
		error("{} has a leading or trailing space.".format(string))
		return

	i = 0
	while i < len(string):
		for s in symbols: # symbols must be sorted in reverse length order
			if string[i:i+len(s)] == s:
				yield s
				i += len(s)
				break
		else:
			# No symbol matched.
			left = string[:i]
			right = string[i:]
			if unicodedata.combining(right[0]): right = "◌" + right
			error("[{}] In {}, no valid symbol {}at the start of {}.".format(
				source['id']['govtrack'],
				string,
				("after " + left + " ") if left else "",
				right))
			return []

# Test that the IPA transcriptions use a reasonable
# and consistent sub-set of IPA. Use symbols close to
# what's recognized by Amazon Polly's American English.
ipa_symbols = {
  "b", "d", "d͡ʒ", "ð", "f", "g", "h", "j", "k",
  "l", "m", "n", "ŋ", "p", "ɹ", "ɹ̜", "ɾ", "s", "ʃ", "t",
  "t͡ʃ", "t͡s", "θ", "v", "w", "z", "ʒ",
  "a", "ɐ", # TODO REMOVE?
  "ɑ", "æ", "æ̃", "aɪ", "aʊ", "ɛ", "ə", "eɪ", "ɚ", "ɝ",
  "i", "ɪ", "ɔ", "ɔɪ", "oʊ", "u", "ʊ", "ʌ",
  "d͡z", "o", # TODO REMOVE?
  "ɔ̃",
  "\u0329", # COMBINING VERTICAL LINE BELOW
  "ˈ", # stressed syllable
  " ", # separates multi-word names
}

# Allow COMBINING DOUBLE INVERTED BREVE to appear over
# diphongs.
for c in set(ipa_symbols):
	if len(c) == 2:
		ipa_symbols.add(c[0] + "\u0361" + c[1])

# Perform unicode normalization so that composable characters are composed,
# since we expect all data to be normalized.
ipa_symbols = { unicodedata.normalize("NFC", s) for s in ipa_symbols }

# Sort in reverse length order so that parse_symbols chops off
# multi-glyph symbols before single-glyph symbols.
ipa_symbols = list(sorted(ipa_symbols, key = lambda s : -len(unicodedata.normalize("NFD", s))))

# Check that the IPA transriptions only used the white-listed symbols.
symcount = { }
for member in guide:
	if "ipa" not in member: continue
	for ipa in member["ipa"].split(" // "):
		for s in parse_symbols(ipa, ipa_symbols, member):
			symcount[s] = symcount.get(s, 0) + 1
#print(" ".join(sorted(symcount.keys())))

# Test that the respellings use all and only
# the symbols that we've documented that we
# use.
respelling_vowels = {
	"a", "ah", "air", "aw", "ay",
	"e", "eh", "ee", "er", "ew",
	"i", "ih", "ī",
	"o", "oh", "oi", "oo", "oor", "or", "ow", "oy",
	"u", "uh", "uu",
	"y", "yoo", "yoor", "yr",
}
respelling_consonants = {
	"b", "ch", "d", "f", "g", "h", "j", "k", "kh",
	"l", "m", "n", "ng", "nk", "p", "r", "s", "sh", "t",
	"th", "t͡h", "v", "w", "y", "z", "zh",
}
respelling_symbols = \
	  respelling_vowels \
	| respelling_consonants \
	| { "-", " " } \

# For syllabification checks, define valid English onsets, based on
# the Penn Phonetics Toolkit, by Joshua Tauberer and based on code by Charles Yang,
# plus other onsets in non-Anglican names.
respelling_onsets = {
	'p', 't', 'k', 'b', 'd', 'g', 'f', 'v', 'th', 't͡h', 's', 'z', 'sh', 'ch', 'j', 'zh',
	'm', 'n', 'r', 'l', 'h', 'w', 'y', 'p r', 't r', 'ch r', 'k r', 'b r', 'd r', 'g r', 'f r',
	'th r', 'sh r', 'j r', 'p l', 'k l', 'b l', 'g l', 'f l', 's l', 't w', 'k w', 'd w',
	's w', 's p', 's t', 's k', 's f', 's m', 's n', 'g w', 'sh n', 'sh w', 's p r', 's p l',
	's t r', 'sh t r', 's k r', 's k w', 's k l', 'th w', 'p y', 'k y', 'b y', 'f y',
	'h y', 'v y', 'th y', 'm y', 's p y', 's k y', 'g y', 'h w', 't s', ''
}
def validate_syllable(syl, stressed, source):
	# Check stress --- all phonemes must be uppercase or all lowercase.
	if syl == syl.upper():
		stressed = True
	elif syl == syl.lower():
		# Might be stressed if it's a single-syllable word.
		pass
	else:
		error("invalid casing in " + word)

	# Force to lowercase.
	syl = syl.lower()

	# Split syllable into phonemes.
	syl = list(parse_symbols(syl, respelling_symbols, source))

	# Split syllable into onset, nucleus, and coda.
	onset = []
	nucleus = []
	coda = []
	for p in syl:
		if p.lower() in respelling_vowels:
			if coda:
				error("invalid syllable structure " + str(syl))
			else:
				nucleus.append(p)
		elif p.lower() in respelling_consonants:
			if nucleus:
				coda.append(p)
			else:
				onset.append(p)
		else:
			raise ValueError(p)

	# Validate onset and nucleus.
	onset = " ".join(onset)
	if onset.lower() not in respelling_onsets:
		error("invalid syllable structure: {} not a valid onset in {} in {}".format(onset, syl, source['id']['govtrack']))
	if onset and not nucleus and onset != "m": # 'm' can be syllabic
		error("invalid syllable structure: onset without nucleus {} in {}".format(onset, source['id']['govtrack']))

	# Josh's "tr"s are like "chr" but that's hard to understand, so force to "tr".
	if "ch r" in onset and stressed:
		error("'chr' should be 'tr' in {} in {}".format(syl, source['id']['govtrack']))

	# Short vowels should be in their "_H" form in open syllables
	# and their regular forms in closed syllables. But 'a' has no
	# separate open-syllable form, 'oh' has no separate closed
	# syllable form, and 'ah' alternates with 'o' but not based on
	# open/closed syllable.
	if ("e" in nucleus or "i" in nucleus or "o" in nucleus or "u" in nucleus) and not coda:
		error("'a/e/i/o/u' in open syllable should be 'ah/eh/ih/oh/oh' in {} in {}".format(syl, source['id']['govtrack']))
	if ("eh" in nucleus or "ih" in nucleus or "uh" in nucleus) and coda:
		error("'ah/eh/ih/oh/uh' in closed syllable should be 'a/e/i/o/o' in {} in {}".format(syl, source['id']['govtrack']))

	# Some respelling symbols are limited in their context.
	if "o" in nucleus and coda and ("r" in coda or "l" in coda):
		error("'o' not allowed in closed syllables with 'r' or 'l' in {} in {}".format(syl, source['id']['govtrack']))
	if "ah" in nucleus and coda and not ("r" in coda or "l" in coda) and syl != ["w", "ah", "n"]:
		error("'ah' not allowed in closed syllable except ones with 'r'/'l' in {} in {}".format(syl, source['id']['govtrack']))
	if "ss" in onset:
		error("'ss' not allowed in onset in {} in {}".format(syl, source['id']['govtrack']))
	if coda == ["s"]:
		error("'s' as entire coda should be 'ss' in {} in {}".format(syl, source['id']['govtrack']))


# Perform unicode normalization so that composable characters are composed.
respelling_symbols = { unicodedata.normalize("NFC", s) for s in respelling_symbols }

# Sort in reverse length order so that parse_symbols chops off
# multi-glyph symbols before single-glyph symbols.
respelling_symbols = list(sorted(respelling_symbols, key = lambda s : -len(unicodedata.normalize("NFD", s))))

word_respellings = defaultdict(lambda : set())

for member in guide:
	for respell in member["respell"].split(" // "):
		# Check that only valid respelling letter( combination)s are present.
		parse_symbols(respell, respelling_symbols, member)

		# Check capitalization - each syllable must be either upper or lower
		# and in each word exactly one syllable must have primary stress
		# unless it's only one syllable and then none are indicated so.
		for word in respell.split(" "):
			syls = word.split("-")
			for syl in syls:
				# Check that the syllabification is valid. Check each
				# syllable's onset and nucleus and that the stress
				# is consistent across the phonemes.
				validate_syllable(syl, len(syls) == 1, member)
			if len(syls) == 1 and word == word.upper():
				error("Single-syllable word should not be represented in uppercase: " + word)
			if len(syls) > 1 and len([syl for syl in syls if syl == syl.upper()]) != 1:
				error("Word should have exactly one primary-stressed syllable: " + word)


	# Check that the respelling has the same number of name/word parts as the original name.
	name = member["name"].split(" // ")
	respell = member["respell"].split(" // ")
	if len(name) != len(respell):
		error("Respelling doesn't have the same number of name parts as the name: {} and {}".format(name, respell))
	else:
		for name, respell in zip(name, respell):
			nw = re.split("[ -]", name) # dashes and spaces are all broken out...
			rw = respell.split(" ") # only as spaces
			if len(nw) != len(rw):
				error("Respelling doesn't have the same number of words as the name: {} and {}".format(nw, rw))
			else:
				for n, r in zip(nw, rw):
					word_respellings[n].add(r)

# Report if any words have different respellings.
for w, rr in word_respellings.items():
	if len(rr) > 1:
		error("Multiple respellings for {}: {}".format(w, ", ".join(rr)))

# Check that we have a record for all current members of Congress and that
# names match.
in_guide = { m["id"]["govtrack"] for m in guide }
M = rtyaml.load(urllib.request.urlopen("https://raw.githubusercontent.com/unitedstates/congress-legislators/master/legislators-current.yaml"))
for m in M:
	if m["id"]["govtrack"] not in in_guide:
		print("No pronunciation guide entry for:")
		print(rtyaml.dump([{ "id": { "govtrack": m["id"]["govtrack"] },
		                    "name": m["name"]["first"] + " // " + m["name"]["last"],
		                    "respell": "" }]))
