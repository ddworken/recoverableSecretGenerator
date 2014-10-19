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
* Correct misspelled words or mis-capitalized words to correct words through comparisons to list of correct words. 
* Correct bits of entropy calculation to account for incorrect ordering and loss of one word. 

#Note: This program is still in alpha and non-backwards compatible changes are likely. 

