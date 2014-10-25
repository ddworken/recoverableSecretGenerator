brainwalletv2.py is a new brainwallet scheme based off of the original brainwallet scheme. Instead of a simple sha256 hash being used to generate the brainwallet, 800 rounds of scrypt are used to generate the address key pair. 100 rounds of scrypt are done on the password+checksum+salt per run, 8 times (allowing multithreading) and then concatenated together before a final sha256. 

```(trusty)david@localhost:~/recoverableSecretGenerator/exampleUsages$ python brainwalletv2.py ```

```Input the password: ```test

```Input the checksum: ```respon

```Your correct checksum is: responsive```

```You forgot the word: travesty```

```Your correct password is: tempest travesty```

```Checksum verified.```

```Hashing...```

```Private key: 5JevwHt1sPkYTyNoR1JfEBwcix9p66qDn9H7XzitnGEaAgCdYsi```

```Address: 1GAA2YyoAjoDefde1wdQFF2iZaEugqwnsE```
