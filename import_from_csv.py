# Import data from CSV.

import sys, collections, csv, rtyaml

# Read existing data.
with open("legislators.yaml") as f:
	guide = rtyaml.load(f)

# Map GovTrack IDs to indexes of existing records.
by_govtrack_id = {
	person["id"]["govtrack"]: i
	for i, person in enumerate(guide)
}

# Map bioguide IDs to GovTrack IDs.
bioguide_to_govtrack = {
	p["id"]["bioguide"]: p["id"]["govtrack"]
	for p in rtyaml.load(open("../congress-legislators/legislators-current.yaml"))
	       + rtyaml.load(open("../congress-legislators/legislators-historical.yaml")) # sometimes the timing of updates is off
}

# Read the CSV data.
for rec in csv.DictReader(sys.stdin):
	if rec["ID"] not in bioguide_to_govtrack:
		print(rec)
		continue

	# Make a new record.
	p = collections.OrderedDict([
		("id", { "govtrack": bioguide_to_govtrack[rec["ID"]] }),
		("name", "{} // {}".format(rec['First'], rec['Last'])),
		("ipa", "{} // {}".format(rec['IPAFirst'], rec['IPALast'])),
		("respell", "{} // {}".format(rec['RespellFirst'], rec['RespellLast'])),
		("notes", rec['Notes']),
	])

	# Replace legislator if already exists.
	if p["id"]["govtrack"] in by_govtrack_id:
		guide[by_govtrack_id[p["id"]["govtrack"]]] = p
	else:
		# Otherwise append.
		guide.append(p)

# Write out update.
with open("legislators.yaml", "w") as f:
	f.write(rtyaml.dump(guide))

