BTCKeyGeneration.py generates a BTC private key address pair in a deterministic manner from the supplied password and checksum. It does so by running the recovery algorithms on the supplied password and checksum, followed by running the full password through a brainwallet generator. 

Usage: 

```(trusty)david@localhost:~/gitSecretInWords/s/passwordGen$ python BTCKey.py 

Input the password: barbecue goggles neptune trojan trombonist universe

Input the checksum: responsive

Checksum verified.

Private key: 5K3EE6bFKcjYdnjx3fqRNWcDRGQy1RK4LU5ougm7YxZQtCTPXXY

Address: 1DGd3W6crQXxKpy2ohi5VjEKqHHJxT7wMr
