import unicodedata
import urllib.request
import re
import rtyaml

with open("legislators.yaml") as f:
	guide = rtyaml.load(f)

def error(msg):
	print(msg)

def check_symbols(string, symbols):
	# check that string is already NFC normalized
	if string != unicodedata.normalize("NFC", string):
		error("{} is not Unicode NFC-normalized.".format(string))
		return

	i = 0
	while i < len(string):
		for s in symbols: # symbols must be sorted in reverse length order
			if string[i:i+len(s)] == s:
				i += len(s)
				break
		else:
			# No symbol matched.
			left = string[:i]
			right = string[i:]
			if unicodedata.combining(right[0]): right = "◌" + right
			error("In {}, no valid symbol {}at the start of {}.".format(
				string,
				("after " + left + " ") if left else "",
				right))
			return

# Test that the IPA transcriptions use a reasonable
# and consistent sub-set of IPA. Use symbols close to
# what's recognized by Amazon Polly's American English.
ipa_symbols = {
  "b", "d", "d͡ʒ", "ð", "f", "g", "h", "j", "k",
  "l", "m", "n", "ŋ", "p", "ɹ", "ɾ", "s", "ʃ", "t",
  "t͡ʃ", "t͡s", "θ", "v", "w", "z", "ʒ",
  "a", "ɐ", # TODO REMOVE?
  "ɑ", "æ", "æ̃", "aɪ", "aʊ", "ɛ", "ə", "eɪ", "ɚ", "ɝ",
  "i", "ɪ", "ɔ", "ɔɪ", "oʊ", "u", "ʊ", "ʌ",
  "o", # TODO REMOVE?
  "'",
  "\u0329", # COMBINING VERTICAL LINE BELOW
  " ", # separates multi-word names
}

# Allow COMBINING DOUBLE INVERTED BREVE to appear over
# diphongs.
for c in set(ipa_symbols):
	if len(c) == 2:
		ipa_symbols.add(c[0] + "\u0361" + c[1])

# Perform unicode normalization so that composable characters are composed.
ipa_symbols = { unicodedata.normalize("NFC", s) for s in ipa_symbols }

# Sort in reverse length order so that check_symbols chops off
# multi-glyph symbols before single-glyph symbols.
ipa_symbols = list(sorted(ipa_symbols, key = lambda s : -len(unicodedata.normalize("NFD", s))))

for member in guide:
	for ipa in member["ipa"].split(" // "):
		pass # check_symbols(ipa, ipa_symbols)

# Test that the respellings use all and only
# the symbols that we've documented that we
# use.
respelling_symbols = {
	"a", "ah", "air", "ar", "aw", "ay",
	"e", "ee", "eer", "er", "ew", "i", "ī",
	"o", "oh", "oi", "oo", "oor", "or", "ow", "oy",
	"u", "uh", "uu", "y", "yoo", "yoor", "yr",

	"b", "ch", "d", "f", "g", "h", "j", "k", "kh",
	"l", "m", "n", "ng", "nk", "p", "r", "s", "t",
	"th", "t͡h", "v", "w", "y", "z", "zh",

	"-", " ",
}

# Perform unicode normalization so that composable characters are composed.
respelling_symbols = { unicodedata.normalize("NFC", s) for s in respelling_symbols }

# Add uppercase of all the lowercase entries above.
for s in set(respelling_symbols): respelling_symbols.add(s.upper())

# Sort in reverse length order so that check_symbols chops off
# multi-glyph symbols before single-glyph symbols.
respelling_symbols = list(sorted(respelling_symbols, key = lambda s : -len(unicodedata.normalize("NFD", s))))

for member in guide:
	for respell in member["respell"].split(" // "):
		# Check that only valid respelling letter( combination)s are present.
		check_symbols(respell, respelling_symbols)

		# Check capitalization - each syllable must be either upper or lower
		# and in each word exactly one syllable must have primary stress
		# unless it's only one syllable and then none are indicated so.
		for word in respell.split(" "):
			syls = word.split("-")
			nstr = 0
			for syl in syls:
				if syl == syl.upper():
					nstr += 1
				elif syl == syl.lower():
					pass
				else:
					error("invalid casing in " + word)
			if len(syls) == 1 and nstr > 0:
				error("Single-syllable word should not be represented in uppercase: " + word)
			if len(syls) > 1 and nstr != 1:
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
			

# Check that we have a record for all current members of Congress and that
# names match.
in_guide = { m["id"]["govtrack"] for m in guide }
M = rtyaml.load(urllib.request.urlopen("https://raw.githubusercontent.com/unitedstates/congress-legislators/master/legislators-current.yaml"))
for m in M:
	if m["id"]["govtrack"] not in in_guide:
		print("No pronunciation guide entry for:")
		print(rtyaml.dump(m))
