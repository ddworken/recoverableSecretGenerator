#!/bin/python
import ecdsa
import hashlib
import binascii
import random

CURVE_TYPE = ecdsa.curves.SECP256k1
BASE_58_CHARS = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
BASE_58_CHARS_LEN = len(BASE_58_CHARS)
MAINNET_PREFIX = '80'

###BTC Generation Library Start: Github Gist=https://gist.github.com/stequald/7e3b15c904e309dec646

def numToWIF(numPriv):
    privKeyHex = MAINNET_PREFIX+hex(numPriv)[2:].strip('L').zfill(64)
    privKeySHA256Hash = hashlib.sha256(binascii.unhexlify(privKeyHex)).hexdigest()
    privKeyDoubleSHA256Hash = hashlib.sha256(binascii.unhexlify(privKeySHA256Hash)).hexdigest()
    checksum = privKeyDoubleSHA256Hash[:8]
    wifNum = int(privKeyHex + checksum, 16)

    # convert number to base58
    base58CharList = []
    for i in range(100):
        base58CharList.append(BASE_58_CHARS[wifNum/(BASE_58_CHARS_LEN**i)%BASE_58_CHARS_LEN])

    # convert character list to string, reverse string, and strip extra leading 1's
    return ''.join(base58CharList)[::-1].lstrip('1')


def WIFToNum(wifPriv):
    numPriv = 0
    for i in range(len(wifPriv)):
        numPriv += BASE_58_CHARS.index(wifPriv[::-1][i])*(BASE_58_CHARS_LEN**i)

    numPriv = numPriv/(2**32)%(2**256)
    return numPriv


def isValidWIF(wifPriv):
    return numToWIF(WIFToNum(wifPriv)) == wifPriv

def numToAddress(numPriv):
    pko = ecdsa.SigningKey.from_secret_exponent(numPriv, CURVE_TYPE)
    pubkey = binascii.hexlify(pko.get_verifying_key().to_string())
    pubkeySHA256Hash = hashlib.sha256(binascii.unhexlify('04' + pubkey)).hexdigest()
    pubkeySHA256RIPEMD160Hash = hashlib.new('ripemd160', binascii.unhexlify(pubkeySHA256Hash)).hexdigest()

    hash1 = hashlib.sha256(binascii.unhexlify('00' + pubkeySHA256RIPEMD160Hash)).hexdigest()
    hash2 = hashlib.sha256(binascii.unhexlify(hash1)).hexdigest()
    checksum = hash2[:8]

    encodedPubKeyHex = pubkeySHA256RIPEMD160Hash + checksum
    encodedPubKeyNum = int(encodedPubKeyHex, 16)

    base58CharIndexList = []
    while encodedPubKeyNum != 0:
        base58CharIndexList.append(encodedPubKeyNum % BASE_58_CHARS_LEN)
        encodedPubKeyNum /= BASE_58_CHARS_LEN

    m = 0
    while encodedPubKeyHex[0 + m : 2 + m] == '00':
        base58CharIndexList.append(0)
        m = m + 2

    address = ''
    for i in base58CharIndexList:
        address = BASE_58_CHARS[i] + address

    return '1' + address

###BTC Generation Library Stop

def randstr(length):
    randomString = ''
    for i in range(0, length):
        randomString.join(chr(random.randint(0,255)))
    return

def numToPubKey(numPriv):
    pko = ecdsa.SigningKey.from_secret_exponent(numPriv, CURVE_TYPE)
    pubkey = binascii.hexlify(pko.get_verifying_key().to_string())
    pubkeySHA256Hash = hashlib.sha256(binascii.unhexlify('04' + pubkey)).hexdigest()
    pubkeySHA256RIPEMD160Hash = hashlib.new('ripemd160', binascii.unhexlify(pubkeySHA256Hash)).hexdigest()

    hash1 = hashlib.sha256(binascii.unhexlify('00' + pubkeySHA256RIPEMD160Hash)).hexdigest()
    hash2 = hashlib.sha256(binascii.unhexlify(hash1)).hexdigest()
    checksum = hash2[:8]

    encodedPubKeyHex = pubkeySHA256RIPEMD160Hash + checksum
    return encodedPubKeyHex