passwordGen
===========
Generate random passwords with an included checksum. Generates random passwords from a random selection of words from PGP's word list. The number of words generated is defined by the bits of entropy requested. A checksum word is also generated at the end to ensure proper transmission of the data. 

###Usage

Basic usage to generate a random word password with 50 bits of entropy and a checksum: 

```python passwordGen.py --bits 56```

If you want to generate a password with characters instead of words (less memorable but shorter): 

```python passwordGen.py --bits 56 --type character```

If you want to verify a password's checksum: 

```python passwordGen.py --verify True --password "Your password made of phrases with no trailing or leading spaces" --checksum "checksum"```

###To Do: 
* When verifying password, sort alphabetically to remove need for password to be remembered in correct order. 
* Add ability to forget one word and recover one word from other words. 
  * Stop using mod in checksum generation, need to embed full number (e.g. 1721 rather than 185). With this, one can recover any missing words via calculating ```$valueOfForgottenWord = $fullChecksumNumber - ($valueOfWord1 + $valueOfWord2 + $valueOfWord3 + $valueOfWord4 + $valueOfWord5)```
* When passwords contain words not in the wordlist, use above to recover the mis-remembered word. 

#Note: This program is still in alpha and non-backwards compatible changes are likely. 

