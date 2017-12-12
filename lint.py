import unicodedata
import rtyaml

with open("legislators.yaml") as f:
	guide = rtyaml.load(f)

# Perform Unicode NFC normalization.
for member in guide:
	for section in ("name", "ipa", "respell"):
		# NFC normalize.
		member[section] = unicodedata.normalize("NFC", member[section])

		# Some symbols are doubled up and leave an extra one after NFC.
		member[section] = member[section].replace('̄', '')

with open("legislators.yaml", "w") as f:
	f.write(rtyaml.dump(guide))

