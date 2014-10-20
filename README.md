passwordGen
===========
Generate random passwords with an included checksum/parity word. Passwords will be generated to give X bits of entropy. Passwords are made to be easily stored in human memory. This is done through using the PGP word list (specially chosen distinct words), allowing incorrect ordering of words, and allowing authentication when up to one word is missing. 

###Usage

Basic usage to generate a random word password with 56 bits of entropy and a checksum: 

```python passwordGen.py --bits 56```

If you want to verify a password's checksum: 

```python passwordGen.py --verify True --password "Your password made of phrases with no trailing or leading spaces" --checksum "checksum"```

If the above is used with an incorrect password, then the word will automatically be recovered for the user. 

authenticate.py provides example code for the usage of this module for verifying authentication via a sha256 hash and this password generation method. 

###To Do: 
* Correct misspelled words to correct words through Levenshtein distance. (Use python-Levenshtein)

###Notes: 
* This program is still in alpha and non-backwards compatible changes are likely. 
* The bits of entropy calculation is only a rough estimate. This is because the math needed to solve for words needed given a certain number of bits, requires a series of complex calculations based off of each case. 
  * E.g. for 5 words, one must calculate the possibilities of 1 of a kind, 2 of a kind, 2 of a kind and 2 of a kind, 2 of a kind and 3 of a kind, 4 of a kind, and 5 of a kind. Generalizing this for up to n words, requires a complex understanding of Partitions (number theory concept). As I lack this background, I am continuing to use this rought approximation. 
