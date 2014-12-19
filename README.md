Error Correcting Secret Generator
===========
Generate random passwords with an included checksum/parity word. Passwords will be generated to give X bits of entropy. Passwords are made to be easily stored in human memory. This is done through using the PGP word list (specially chosen distinct words), allowing incorrect ordering of words, allowing authentication when up to one word is missing, and using Levenshtein distance matching to correct incorrect words. 

This program was inspired by Microsoft's research paper on the topic of [Reliable Storage of 56-bit Secrets in Humany Memory](http://research.microsoft.com/pubs/220380/SecretsInHumanMemory_Extended.pdf). This program improves on the work done in this paper by allowing for a variety of common errors in human memory to occur. 

###Usage

Basic usage to generate a random word password with 56 bits of entropy and a checksum: 

```python passwordGen.py --bits 56```

If you want to verify a password's checksum: 

```python passwordGen.py --verify True --password "Your password made of phrases with no trailing or leading spaces" --checksum "checksum"```

If the above is used with an incorrect password, then the word will automatically be recovered for the user. 

###Installation

    sudo apt-get install python-dev libssl-dev
    git clone https://github.com/ddworken/recoverableSecretGenerator.git
    cd recoverableSecretGenerator
    sudo pip -r requirements.txt

