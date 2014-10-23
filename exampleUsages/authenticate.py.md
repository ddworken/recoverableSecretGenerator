authenticate.py provides example code for the usage of this module for verifying authentication via a sha256 hash and this password generation method. Example Usage: 

```(trusty)david@localhost:~/passwordGen$ python authenticate.py```

```Input the password: ```barbecue goggles neptune trojn trombonist   

```Input the checksum: ```responsive

```trojn is not in the word list!```

```You forgot the word: universe```

```Your correct password is: barbecue goggles neptune trojan trombonist universe```

```Checksum verified.```

```Access Granted!```

authenticate.py will authenticate a user against a prestored sha256 hash of the password. 
