Prononciation Guide for Names of Members of Congress
====================================================

This project contains a pronunciation guide for the names of current and recent-past Members of the United States Congress.

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

`name` provides the `first` and `last` name of the Member of Congress, as used by this project.

`ipa` provides the pronunciation of the name using the [International Phonetic Alphabet](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) the world-wide standard for transcribing the sounds of speech. An IPA transcription is provided for each of the `first` and `last` names as stored in the `name` fields.

`respell` provides a friendly guide to the pronunciation of the name using a "[respelling](https://en.wikipedia.org/wiki/Pronunciation_respelling_for_English)". A respelling is provided for each of the `first` and `last` names as stored in the `name` fields. We use a respelling guide similar to the [Pocket Oxford English Dictionary](https://www.amazon.com/Pocket-Oxford-English-Dictionary-Dictionaries/dp/0199666156/ref=sr_1_5?ie=UTF8&qid=1508765253&sr=8-5&keywords=pocket+oxford):

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
| eer   | beer    | kh        | lock    |
| er    | her     | l         | leg     |
| ew    | few     | m         | man     |
| i     | pin     | n         | not     |
| ī     | eye     | ng        | sing    |
| o     | top     | nk        | thank   |
| oh    | most    | p         | pen     |
| oi    | join    | r         | rag     |
| oo    | soon    | s         | sit     |
| oor   | poor    | t         | top     |
| or    | corn    | th        | thin    |
| ow    | cow    | t͡h        | this    |
| oy    | boy     | v         | van     |
| u     | cup     | w         | will    |
| uh    | 'a' in along     | y         | yes     |
| uu    | book     | z         | zebra   |
| y     | cry     | zh        | vision  |
| yoo   | unit
| yoor  | Europe
| yr    | fire

In addition, capitalization is used to indicate primary stress, syllables are separated by dashes, and multi-word names, whether separated by dashes or spaces, are broken out by spaces.