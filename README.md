passwordGen
===========
Generate random passwords with an included checksum. Generates random passwords from a random selection of words from PGP's word list. The number of words generated is defined by the bits of entropy requested. A checksum word is also generated at the end to ensure proper transmission of the data. 

##Usage

Basic usage to generate a random word password with 50 bits of entropy and a checksum: 

```python passwordGen.py --bits 56```

If you want to generate a password with characters instead of words (less memorable but shorter): 

```python passwordGen.py --bits 56 --type character```

If you want to verify a password's checksum: 

```python passwordGen.py --verify True --password "Your password made of phrases with no trailing or leading spaces" --checksum "checksum"```
