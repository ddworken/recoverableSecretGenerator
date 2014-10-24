#!/bin/python
import hashlib
import Levenshtein
import binascii
import ecdsa 

CURVE_TYPE = ecdsa.curves.SECP256k1
BASE_58_CHARS = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
BASE_58_CHARS_LEN = len(BASE_58_CHARS)
MAINNET_PREFIX = '80'

###BTC Generation Start: Github Gist=https://gist.github.com/stequald/7e3b15c904e309dec646

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
                base58CharIndexList.append(0);
                m = m + 2;
 
        address = ''
        for i in base58CharIndexList:
                address = BASE_58_CHARS[i] + address

        return '1' + address

###BTC Generation Stop

def containsBadWords(password):
        passwordList = password.split(" ")
        for i in range(0, len(passwordList)):
                if passwordList[i] not in wordList: 
                        #print passwordList[i] + " is not in the word list!"
                        return True
        return False

def fixPasswordWithBadWords(password):
        bestMatch = ""
        bestMatchDistance = 0
        passwordList = password.split(" ")
        for i in range(0, len(passwordList)):
                for j in range(0, len(wordList)):
                        if Levenshtein.ratio(passwordList[i], wordList[j]) > bestMatchDistance:
                                bestMatch = wordList[j]
                                bestMatchDistance = Levenshtein.ratio(passwordList[i], wordList[j])
                                #print "Set bestMatch to " + wordList[j]
                                #print "set bestMatchDistance to " + str(bestMatchDistance)
                #print passwordList[i] + " was corrected to " + bestMatch
                passwordList[i] =  bestMatch 
                bestMatch = ""
                bestMatchDistance = 0
        passwordList.sort()
        password = ' '.join(passwordList)
        return password

def sortPasswordString(password):
        passwordList = password.split(" ")
        passwordList.sort()
        password = ' '.join(passwordList)
        return password

def genWordChecksum(password):
        sum = 0;
        passwordList = password.split(" ")
        for i in range(0, len(passwordList)): 
                sum += wordList.index(passwordList[i])
        modSum = sum % len(wordList)
        return wordList[modSum]

def recoverWord(password, checksum): 
        recoveredWord = str(wordList[int((wordList.index(checksum)+len(wordList))-wordList.index(genWordChecksum(password))) % len(wordList)])
        return recoveredWord

def genKeys(password, checksum): 
        password = password.lower()
        if containsBadWords(password):
                password = fixPasswordWithBadWords(password)
        if containsBadWords(checksum):
                checksum = fixPasswordWithBadWords(checksum)
                print "Your correct checksum is: " + checksum
        if genWordChecksum(password) != checksum:
                print "You forgot the word: " + recoverWord(password, checksum)
                forgottenWord = recoverWord(password, checksum)
                password += " "
                password += forgottenWord
                password = sortPasswordString(password)
                print "Your correct password is: " + password
        print "Checksum verified."
        num = int(hashlib.sha256(password+checksum).hexdigest(), 16)
        privateKey = numToWIF(num)
        address = numToAddress(num)
        assert isValidWIF(privateKey) == True
        print "Private key: " + str(privateKey)
        print "Address: " + str(address)

wordList = ["aardvark", "adroitness", "absurd", "adviser", "accrue", "aftermath", "acme", "aggregate", "adrift", "alkali", "adult", "almighty", "afflict", "amulet", "ahead", "amusement", "aimless", "antenna", "algol", "applicant", "allow", "apollo", "alone", "armistice", "ammo", "article", "ancient", "asteroid", "apple", "atlantic", "artist", "atmosphere", "assume", "autopsy", "athens", "babylon", "atlas", "backwater", "aztec", "barbecue", "baboon", "belowground", "backfield", "bifocals", "backward", "bodyguard", "banjo", "bookseller", "beaming", "borderline", "bedlamp", "bottomless", "beehive", "bradbury", "beeswax", "bravado", "befriend", "brazilian", "belfast", "breakaway", "berserk", "burlington", "billiard", "businessman", "bison", "butterfat", "blackjack", "camelot", "blockade", "candidate", "blowtorch", "cannonball", "bluebird", "capricorn", "bombast", "caravan", "bookshelf", "caretaker", "brackish", "celebrate", "breadline", "cellulose", "breakup", "certify", "brickyard", "chambermaid", "briefcase", "cherokee", "burbank", "chicago", "button", "clergyman", "buzzard", "coherence", "cement", "combustion", "chairlift", "commando", "chatter", "company", "checkup", "component", "chisel", "concurrent", "choking", "confidence", "chopper", "conformist", "christmas", "congregate", "clamshell", "consensus", "classic", "consulting", "classroom", "corporate", "cleanup", "corrosion", "clockwork", "councilman", "cobra", "crossover", "commence", "crucifix", "concert", "cumbersome", "cowbell", "customer", "crackdown", "dakota", "cranky", "decadence", "crowfoot", "december", "crucial", "decimal", "crumpled", "designing", "crusade", "detector", "cubic", "detergent", "dashboard", "determine", "deadbolt", "dictator", "deckhand", "dinosaur", "dogsled", "direction", "dragnet", "disable", "drainage", "disbelief", "dreadful", "disruptive", "drifter", "distortion", "dropper", "document", "drumbeat", "embezzle", "drunken", "enchanting", "dupont", "enrollment", "dwelling", "enterprise", "eating", "equation", "edict", "equipment", "egghead", "escapade", "eightball", "eskimo", "endorse", "everyday", "endow", "examine", "enlist", "existence", "erase", "exodus", "escape", "fascinate", "exceed", "filament", "eyeglass", "finicky", "eyetooth", "forever", "facial", "fortitude", "fallout", "frequency", "flagpole", "gadgetry", "flatfoot", "galveston", "flytrap", "getaway", "fracture", "glossary", "framework", "gossamer", "freedom", "graduate", "frighten", "gravity", "gazelle", "guitarist", "geiger", "hamburger", "glitter", "hamilton", "glucose", "handiwork", "goggles", "hazardous", "goldfish", "headwaters", "gremlin", "hemisphere", "guidance", "hesitate", "hamlet", "hideaway", "highchair", "holiness", "hockey", "hurricane", "indoors", "hydraulic", "indulge", "impartial", "inverse", "impetus", "involve", "inception", "island", "indigo", "jawbone", "inertia", "keyboard", "infancy", "kickoff", "inferno", "kiwi", "informant", "klaxon", "insincere", "locale", "insurgent", "lockup", "integrate", "merit", "intention", "minnow", "inventive", "miser", "istanbul", "mohawk", "jamaica", "mural", "jupiter", "music", "leprosy", "necklace", "letterhead", "neptune", "liberty", "newborn", "maritime", "nightbird", "matchmaker", "oakland", "maverick", "obtuse", "medusa", "offload", "megaton", "optic", "microscope", "orca", "microwave", "payday", "midsummer", "peachy", "millionaire", "pheasant", "miracle", "physique", "misnomer", "playhouse", "molasses", "pluto", "molecule", "preclude", "montana", "prefer", "monument", "preshrunk", "mosquito", "printer", "narrative", "prowler", "nebula", "pupil", "newsletter", "puppy", "norwegian", "python", "october", "quadrant", "ohio", "quiver", "onlooker", "quota", "opulent", "ragtime", "orlando", "ratchet", "outfielder", "rebirth", "pacific", "reform", "pandemic", "regain", "pandora", "reindeer", "paperweight", "rematch", "paragon", "repay", "paragraph", "retouch", "paramount", "revenge", "passenger", "reward", "pedigree", "rhythm", "pegasus", "ribcage", "penetrate", "ringbolt", "perceptive", "robust", "performance", "rocker", "pharmacy", "ruffled", "phonetic", "sailboat", "photograph", "sawdust", "pioneer", "scallion", "pocketful", "scenic", "politeness", "scorecard", "positive", "scotland", "potato", "seabird", "processor", "select", "provincial", "sentence", "proximate", "shadow", "puberty", "shamrock", "publisher", "showgirl", "pyramid", "skullcap", "quantity", "skydive", "racketeer", "slingshot", "rebellion", "slowdown", "recipe", "snapline", "recover", "snapshot", "repellent", "snowcap", "replica", "snowslide", "reproduce", "solo", "resistor", "southward", "responsive", "soybean", "retraction", "spaniel", "retrieval", "spearhead", "retrospect", "spellbind", "revenue", "spheroid", "revival", "spigot", "revolver", "spindle", "sandalwood", "spyglass", "sardonic", "stagehand", "saturday", "stagnate", "savagery", "stairway", "scavenger", "standard", "sensation", "stapler", "sociable", "steamship", "souvenir", "sterling", "specialist", "stockman", "speculate", "stopwatch", "stethoscope", "stormy", "stupendous", "sugar", "supportive", "surmount", "surrender", "suspense", "suspicious", "sweatband", "sympathy", "swelter", "tambourine", "tactics", "telephone", "talon", "therapist", "tapeworm", "tobacco", "tempest", "tolerance", "tiger", "tomorrow", "tissue", "torpedo", "tonic", "tradition", "topmost", "travesty", "tracker", "trombonist", "transit", "truncated", "trauma", "typewriter", "treadmill", "ultimate", "trojan", "undaunted", "trouble", "underfoot", "tumor", "unicorn", "tunnel", "unify", "tycoon", "universe", "uncut", "unravel", "unearth", "upcoming", "unwind", "vacancy", "uproot", "vagabond", "upset", "vertigo", "upshot", "virginia", "vapor", "visitor", "village", "vocalist", "virus", "voyager", "vulcan", "warranty", "waffle", "waterloo", "wallet", "whimsical", "watchword", "wichita", "wayside", "wilmington", "willow", "wyoming", "woodlark", "yesteryear", "zulu", "yucatan"]
genKeys(raw_input("Input the password: "), raw_input("Input the checksum: "))
