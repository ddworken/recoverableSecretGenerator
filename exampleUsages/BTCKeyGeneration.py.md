BTCKeyGeneration.py generates a BTC private key address pair in a deterministic manner from the supplied password and checksum. It does so by running the recovery algorithms on the supplied password and checksum, followed by running the full password through a brainwallet generator. 

Usage: 

```(trusty)david@localhost:~/passwordGen/exampleUsages/$ python BTCKey.py ```

```Input the password: ```barbecue goggles neptune trojan trombonist universe

```Input the checksum: ```responsive

```Checksum verified.```

```Private key: 5J2VMSchvZ9exa9BEWXubDJgecKwFiUzuDaskRKvrZphGkHy2FV```

```Public key: 58f96ff5a9a1d2e4edb5b807ce139c7179b916c4c5a683ee```

```Address: 197TH6JemVvPCbMiqwZsVHmBFE55nNjpwP```
