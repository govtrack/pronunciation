Prononciation Guide for the Names of Members of Congress
========================================================

This project contains a pronunciation guide for the names of current and recent-past Members of the United States Congress. This is a project of GovTrack.us. The first 539 records were created by Ezra Wyschogrod.

[legislators.yaml](legislators.yaml) is a YAML-formatted file. Each record is a current or recent-past Member of Congress which looks like:

```yaml
- id:
    govtrack: 400623
  name: Debbie // Wasserman Schultz
  ipa: dɛbi // wasɹ̩mən ʃʊlt͡s
  respell: DEH-bee // WASS-er-mun shuults
  notes: https://www.youtube.com/watch?v=ZVmGudgxiRg
```

The record has four parts:

`id`...`govtrack` provides the numeric ID of the Member of Congress on GovTrack.

`name` provides the first and last name of the Member of Congress, as used by this project, separated by `//`.

`ipa` provides the pronunciation of the name using a subset of the [International Phonetic Alphabet](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) the world-wide standard for transcribing the sounds of speech. An IPA transcription is provided for the name as it appears in the `name` field, with the corresponding name parts separated by `//`. We use a subset of IPA, to guide us to transcribing sounds consistently, that consists of the vowels `a ɐ ɑ æ a͡ɪ a͡ʊ ə ɛ ɝ e͡ɪ i ɪ o ɔ ɔ͡ɪ o͡ʊ u ʊ ʌ` and consonants `b d d͡z d͡ʒ f g h j k l m n ŋ p ɹ ɹ̜ ɾ s ʃ t t͡s t͡ʃ θ ʒ v w z`.

`respell` provides a friendly guide to the pronunciation of the name using a "[respelling](https://en.wikipedia.org/wiki/Pronunciation_respelling_for_English)". The respelling is provided for the name as it appears in the `name` field, with the corresponding name parts separated by `//`. We use a respelling guide similar to the [Pocket Oxford English Dictionary](https://www.amazon.com/Pocket-Oxford-English-Dictionary-Dictionaries/dp/0199666156/ref=sr_1_5?ie=UTF8&qid=1508765253&sr=8-5&keywords=pocket+oxford):

| Vowel | Example | Consonant | Example |
| ----- | ------- | --------- | ------- |
| a     | cat     | b         | bat     |
| ah/o  | calm    | ch        | chin    |
| air   | hair    | d         | day     |
|       |         | f         | fun     |
| aw    | law     | g         | get     |
| ay    | say     | h         | hat     |
| e/eh  | bed     | j         | jam     |
| ee    | meet    | k         | king    |
|       |         | l         | leg     |
| er    | her     | m         | man     |
| ew    | few     | n         | not     |
| i/ih  | pin     | ng        | sing    |
| ī     | eye     | nk        | thank   |
|       |         | p         | pen     |
| oh    | most    | r         | rag     |
| oo    | soon    | s/ss      | sit     |
| oor   | poor    | sh        | push    |
| or    | corn    | t         | top     |
| ow    | cow     | th        | thin    |
| oy    | boy     | t͡h        | this    |
| u/uh  | cup     | v         | van     |
| uu    | book    | w         | will    |
|       |         | y         | yes     |
|       |         | z         | zebra   |
|       |         | zh        | vision  |

Constraints:

* For improved readability, some vowels have one form that only appears in closed syllables (e.g. a constant follows the vowel), `e`, `i`, `u`, and a different form that only appears in open syllables (`eh`, `ih`, `uh`). `a` has no separate open syllable form.
* `o` and `ah` are used for the same sound. `o` is used in closed syllables, except ones that end in `r` or `l`, since in open syllables one might think it should be pronounced as in "do", "to", etc., and "dor"/"bold" is a different vowel. `ah` is used in open syllables and closed syllables ending in `r`/`l`.
* `s` is doubled as `ss` in non-complex codas to make it less confusable for a `z` sound. In complex codas, the presence of other consonants with a voice contrast often makes `s` unambiguous.

In addition:

* Syllables are separated by dashes.
* Capitalization is used to indicate primary stress, but in single-syllable words the word is entered in lowercase.
* Multi-word names, whether separated by dashes or spaces, are broken out by spaces.
