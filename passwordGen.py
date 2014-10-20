#!/bin/python
import argparse
import math
from random import randint
parser=argparse.ArgumentParser(description='Randomly generate passwords with a specified amount of entropy.')
parser.add_argument('--bits', dest='bits', help='How many bits of entropy are required.')
parser.add_argument('--verify', dest='verify', help='If argument is  supplied, program will verify checksum. ')
parser.add_argument('--password', dest='password', help='If verify is set to True, then a password must be supplied.')
parser.add_argument('--checksum', dest='checksum', help='The checksum to go with the password supplied.')
args = parser.parse_args()
bits = args.bits


def genWordPassword(bits):
        words = int(math.ceil(int(bits) / math.log(len(wordList), 2)))
        password = ""
        for i in range(0,words):
                rand = randint(1, len(wordList) * 10) % len(wordList)
                password += wordList[rand]
                password += " "
        password = password[:-1]
        return sortPasswordString(password)

def sortPasswordString(password): 
        passwordList = password.split(" ")
        passwordList.sort()
        password = ' '.join(passwordList)
        return password

def genCharPassword(bits):
        chars = int(math.ceil(int(bits) / math.log(26, 2)))
        password = ""
        for i in range(1, chars):
                rand = randint(97, 122)
                password += chr(rand)
        return password

def genWordChecksum(password):
        sum = 0;
        passwordList = password.split(" ")
        for i in range(1, len(passwordList)): 
                sum += wordList.index(passwordList[i])
        modSum = sum % len(wordList)
        return wordList[modSum]

def recoverWord(password, checksum): 
        recoveredWord = str(wordList[int((wordList.index(checksum)+len(wordList))-wordList.index(genWordChecksum(password))) % len(wordList)])
        return recoveredWord

wordList = ["aardvark", "adroitness", "absurd", "adviser", "accrue", "aftermath", "acme", "aggregate", "adrift", "alkali", "adult", "almighty", "afflict", "amulet", "ahead", "amusement", "aimless", "antenna", "Algol", "applicant", "allow", "Apollo", "alone", "armistice", "ammo", "article", "ancient", "asteroid", "apple", "Atlantic", "artist", "atmosphere", "assume", "autopsy", "Athens", "Babylon", "atlas", "backwater", "Aztec", "barbecue", "baboon", "belowground", "backfield", "bifocals", "backward", "bodyguard", "banjo", "bookseller", "beaming", "borderline", "bedlamp", "bottomless", "beehive", "Bradbury", "beeswax", "bravado", "befriend", "Brazilian", "Belfast", "breakaway", "berserk", "Burlington", "billiard", "businessman", "bison", "butterfat", "blackjack", "Camelot", "blockade", "candidate", "blowtorch", "cannonball", "bluebird", "Capricorn", "bombast", "caravan", "bookshelf", "caretaker", "brackish", "celebrate", "breadline", "cellulose", "breakup", "certify", "brickyard", "chambermaid", "briefcase", "Cherokee", "Burbank", "Chicago", "button", "clergyman", "buzzard", "coherence", "cement", "combustion", "chairlift", "commando", "chatter", "company", "checkup", "component", "chisel", "concurrent", "choking", "confidence", "chopper", "conformist", "Christmas", "congregate", "clamshell", "consensus", "classic", "consulting", "classroom", "corporate", "cleanup", "corrosion", "clockwork", "councilman", "cobra", "crossover", "commence", "crucifix", "concert", "cumbersome", "cowbell", "customer", "crackdown", "Dakota", "cranky", "decadence", "crowfoot", "December", "crucial", "decimal", "crumpled", "designing", "crusade", "detector", "cubic", "detergent", "dashboard", "determine", "deadbolt", "dictator", "deckhand", "dinosaur", "dogsled", "direction", "dragnet", "disable", "drainage", "disbelief", "dreadful", "disruptive", "drifter", "distortion", "dropper", "document", "drumbeat", "embezzle", "drunken", "enchanting", "Dupont", "enrollment", "dwelling", "enterprise", "eating", "equation", "edict", "equipment", "egghead", "escapade", "eightball", "Eskimo", "endorse", "everyday", "endow", "examine", "enlist", "existence", "erase", "exodus", "escape", "fascinate", "exceed", "filament", "eyeglass", "finicky", "eyetooth", "forever", "facial", "fortitude", "fallout", "frequency", "flagpole", "gadgetry", "flatfoot", "Galveston", "flytrap", "getaway", "fracture", "glossary", "framework", "gossamer", "freedom", "graduate", "frighten", "gravity", "gazelle", "guitarist", "Geiger", "hamburger", "glitter", "Hamilton", "glucose", "handiwork", "goggles", "hazardous", "goldfish", "headwaters", "gremlin", "hemisphere", "guidance", "hesitate", "hamlet", "hideaway", "highchair", "holiness", "hockey", "hurricane", "indoors", "hydraulic", "indulge", "impartial", "inverse", "impetus", "involve", "inception", "island", "indigo", "jawbone", "inertia", "keyboard", "infancy", "kickoff", "inferno", "kiwi", "informant", "klaxon", "insincere", "locale", "insurgent", "lockup", "integrate", "merit", "intention", "minnow", "inventive", "miser", "Istanbul", "Mohawk", "Jamaica", "mural", "Jupiter", "music", "leprosy", "necklace", "letterhead", "Neptune", "liberty", "newborn", "maritime", "nightbird", "matchmaker", "Oakland", "maverick", "obtuse", "Medusa", "offload", "megaton", "optic", "microscope", "orca", "microwave", "payday", "midsummer", "peachy", "millionaire", "pheasant", "miracle", "physique", "misnomer", "playhouse", "molasses", "Pluto", "molecule", "preclude", "Montana", "prefer", "monument", "preshrunk", "mosquito", "printer", "narrative", "prowler", "nebula", "pupil", "newsletter", "puppy", "Norwegian", "python", "October", "quadrant", "Ohio", "quiver", "onlooker", "quota", "opulent", "ragtime", "Orlando", "ratchet", "outfielder", "rebirth", "Pacific", "reform", "pandemic", "regain", "Pandora", "reindeer", "paperweight", "rematch", "paragon", "repay", "paragraph", "retouch", "paramount", "revenge", "passenger", "reward", "pedigree", "rhythm", "Pegasus", "ribcage", "penetrate", "ringbolt", "perceptive", "robust", "performance", "rocker", "pharmacy", "ruffled", "phonetic", "sailboat", "photograph", "sawdust", "pioneer", "scallion", "pocketful", "scenic", "politeness", "scorecard", "positive", "Scotland", "potato", "seabird", "processor", "select", "provincial", "sentence", "proximate", "shadow", "puberty", "shamrock", "publisher", "showgirl", "pyramid", "skullcap", "quantity", "skydive", "racketeer", "slingshot", "rebellion", "slowdown", "recipe", "snapline", "recover", "snapshot", "repellent", "snowcap", "replica", "snowslide", "reproduce", "solo", "resistor", "southward", "responsive", "soybean", "retraction", "spaniel", "retrieval", "spearhead", "retrospect", "spellbind", "revenue", "spheroid", "revival", "spigot", "revolver", "spindle", "sandalwood", "spyglass", "sardonic", "stagehand", "Saturday", "stagnate", "savagery", "stairway", "scavenger", "standard", "sensation", "stapler", "sociable", "steamship", "souvenir", "sterling", "specialist", "stockman", "speculate", "stopwatch", "stethoscope", "stormy", "stupendous", "sugar", "supportive", "surmount", "surrender", "suspense", "suspicious", "sweatband", "sympathy", "swelter", "tambourine", "tactics", "telephone", "talon", "therapist", "tapeworm", "tobacco", "tempest", "tolerance", "tiger", "tomorrow", "tissue", "torpedo", "tonic", "tradition", "topmost", "travesty", "tracker", "trombonist", "transit", "truncated", "trauma", "typewriter", "treadmill", "ultimate", "Trojan", "undaunted", "trouble", "underfoot", "tumor", "unicorn", "tunnel", "unify", "tycoon", "universe", "uncut", "unravel", "unearth", "upcoming", "unwind", "vacancy", "uproot", "vagabond", "upset", "vertigo", "upshot", "Virginia", "vapor", "visitor", "village", "vocalist", "virus", "voyager", "Vulcan", "warranty", "waffle", "Waterloo", "wallet", "whimsical", "watchword", "Wichita", "wayside", "Wilmington", "willow", "Wyoming", "woodlark", "yesteryear", "Zulu", "Yucatan"]

if args.verify is not None: 
        if args.password is None: 
                print "Error: Must supply password via the --password option."
        if args.checksum is None: 
                print "Error: Must supply chechsum via the --checksum option."
        if genWordChecksum(args.password) == args.checksum: 
                print "Checksums match."
        else: 
                print "Checksums do not match."
        if wordList.index(args.checksum) != wordList.index(genWordChecksum(args.password)): 
                print "You forgot the word: " + recoverWord(args.password, args.checksum)
else: 
        password = genWordPassword(bits);
        print password
        print genWordChecksum(password)
