Prononciation Guide for the Names of Members of Congress
========================================================

This project contains a pronunciation guide for the names of current and recent-past Members of the United States Congress. This is a project of GovTrack.us. The first 539 records were created by Ezra Wyschogrod.

[legislators.yaml](legislators.yaml) is a YAML-formatted file. Each record is a current or recent-past Member of Congress which looks like:

```yaml
- id:
    govtrack: 400623
  name: Debbie // Wasserman Schultz
  ipa: dɛbi // wasɹ̩mən ʃʊlt͡s
  respell: DE-bee // WAS-er-mun shuults
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
| ah    | calm    | ch        | chin    |
| air   | hair    | d         | day     |
| ar    | bar     | f         | fat     |
| aw    | law     | g         | get     |
| ay    | say     | h         | hat     |
| e     | bed     | j         | jam     |
| ee    | meet    | k         | king    |
| eer   | beer    | l         | leg     |
| er    | her     | m         | man     |
| ew    | few     | n         | not     |
| i     | pin     | ng        | sing    |
| ī     | eye     | nk        | thank   |
| o     | top     | p         | pen     |
| oh    | most    | r         | rag     |
| oo    | soon    | s         | sit     |
| oor   | poor    | sh        | push    |
| or    | corn    | t         | top     |
| ow    | cow     | th        | thin    |
| oy    | boy     | t͡h        | this    |
| u/uh  | cup     | v         | van     |
| uu    | book    | w         | will    |
| y     | cry     | y         | yes     |
| yoo   | unit    | z         | zebra   |
| yr    | fire    | zh        | vision  |

We use `u` and `uh` for both the stressed and unstressed mid central vowel, prefering `u` when the syllable has both an onset and a coda for readability reasons.

In addition:

* Syllables are separated by dashes.
* Capitalization is used to indicate primary stress, but in single-syllable names the entire name is lowercase.
* Multi-word names, whether separated by dashes or spaces, are broken out by spaces.
