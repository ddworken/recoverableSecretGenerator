#!/bin/python
import hashlib
import scrypt
from multiprocessing import Pool
import library.BTCLib
import library.mainLib

def repeatedScrypt(password):
    scryptHash = password
    for i in range(1, 100):
        scryptHash = scrypt.hash(scryptHash, '')
    return scryptHash

def genKeys(password, checksum):
    password = password.lower()
    if library.mainLib.containsBadWords(password):
        password = library.mainLib.fixPasswordWithBadWords(password)
    if library.mainLib.containsBadWords(checksum):
        checksum = library.mainLib.fixPasswordWithBadWords(checksum)
        print "Your correct checksum is: " + checksum
    if library.mainLib.genWordChecksum(password) != checksum:
        print "You forgot the word: " + library.mainLib.recoverWord(password, checksum)
        forgottenWord = library.mainLib.recoverWord(password, checksum)
        password += " "
        password += forgottenWord
        password = library.mainLib.sortPasswordString(password)
        print "Your correct password is: " + password
    print "Checksum verified."
    print "Hashing..."
    multicoreList = [password+checksum+"1", password+checksum+"2", password+checksum+"3", password+checksum+"4", password+checksum+"5", password+checksum+"6", password+checksum+"7", password+checksum+"8"]
    pool = Pool()
    scryptOutputList = pool.map(repeatedScrypt, multicoreList)
    scryptHash = ''.join(scryptOutputList)
    num = int(hashlib.sha256(scryptHash).hexdigest(), 16)
    privateKey = library.BTCLib.numToWIF(num)
    publicKey = library.BTCLib.numToPubKey(library.BTCLib.WIFToNum(privateKey))
    address = library.BTCLib.numToAddress(num)
    assert library.BTCLib.isValidWIF(privateKey) == True
    print "Private key: " + str(privateKey)
    print "Address: " + str(address)

hash = ""
wordList = ["aardvark", "adroitness", "absurd", "adviser", "accrue", "aftermath", "acme", "aggregate", "adrift", "alkali", "adult", "almighty", "afflict", "amulet", "ahead", "amusement", "aimless", "antenna", "algol", "applicant", "allow", "apollo", "alone", "armistice", "ammo", "article", "ancient", "asteroid", "apple", "atlantic", "artist", "atmosphere", "assume", "autopsy", "athens", "babylon", "atlas", "backwater", "aztec", "barbecue", "baboon", "belowground", "backfield", "bifocals", "backward", "bodyguard", "banjo", "bookseller", "beaming", "borderline", "bedlamp", "bottomless", "beehive", "bradbury", "beeswax", "bravado", "befriend", "brazilian", "belfast", "breakaway", "berserk", "burlington", "billiard", "businessman", "bison", "butterfat", "blackjack", "camelot", "blockade", "candidate", "blowtorch", "cannonball", "bluebird", "capricorn", "bombast", "caravan", "bookshelf", "caretaker", "brackish", "celebrate", "breadline", "cellulose", "breakup", "certify", "brickyard", "chambermaid", "briefcase", "cherokee", "burbank", "chicago", "button", "clergyman", "buzzard", "coherence", "cement", "combustion", "chairlift", "commando", "chatter", "company", "checkup", "component", "chisel", "concurrent", "choking", "confidence", "chopper", "conformist", "christmas", "congregate", "clamshell", "consensus", "classic", "consulting", "classroom", "corporate", "cleanup", "corrosion", "clockwork", "councilman", "cobra", "crossover", "commence", "crucifix", "concert", "cumbersome", "cowbell", "customer", "crackdown", "dakota", "cranky", "decadence", "crowfoot", "december", "crucial", "decimal", "crumpled", "designing", "crusade", "detector", "cubic", "detergent", "dashboard", "determine", "deadbolt", "dictator", "deckhand", "dinosaur", "dogsled", "direction", "dragnet", "disable", "drainage", "disbelief", "dreadful", "disruptive", "drifter", "distortion", "dropper", "document", "drumbeat", "embezzle", "drunken", "enchanting", "dupont", "enrollment", "dwelling", "enterprise", "eating", "equation", "edict", "equipment", "egghead", "escapade", "eightball", "eskimo", "endorse", "everyday", "endow", "examine", "enlist", "existence", "erase", "exodus", "escape", "fascinate", "exceed", "filament", "eyeglass", "finicky", "eyetooth", "forever", "facial", "fortitude", "fallout", "frequency", "flagpole", "gadgetry", "flatfoot", "galveston", "flytrap", "getaway", "fracture", "glossary", "framework", "gossamer", "freedom", "graduate", "frighten", "gravity", "gazelle", "guitarist", "geiger", "hamburger", "glitter", "hamilton", "glucose", "handiwork", "goggles", "hazardous", "goldfish", "headwaters", "gremlin", "hemisphere", "guidance", "hesitate", "hamlet", "hideaway", "highchair", "holiness", "hockey", "hurricane", "indoors", "hydraulic", "indulge", "impartial", "inverse", "impetus", "involve", "inception", "island", "indigo", "jawbone", "inertia", "keyboard", "infancy", "kickoff", "inferno", "kiwi", "informant", "klaxon", "insincere", "locale", "insurgent", "lockup", "integrate", "merit", "intention", "minnow", "inventive", "miser", "istanbul", "mohawk", "jamaica", "mural", "jupiter", "music", "leprosy", "necklace", "letterhead", "neptune", "liberty", "newborn", "maritime", "nightbird", "matchmaker", "oakland", "maverick", "obtuse", "medusa", "offload", "megaton", "optic", "microscope", "orca", "microwave", "payday", "midsummer", "peachy", "millionaire", "pheasant", "miracle", "physique", "misnomer", "playhouse", "molasses", "pluto", "molecule", "preclude", "montana", "prefer", "monument", "preshrunk", "mosquito", "printer", "narrative", "prowler", "nebula", "pupil", "newsletter", "puppy", "norwegian", "python", "october", "quadrant", "ohio", "quiver", "onlooker", "quota", "opulent", "ragtime", "orlando", "ratchet", "outfielder", "rebirth", "pacific", "reform", "pandemic", "regain", "pandora", "reindeer", "paperweight", "rematch", "paragon", "repay", "paragraph", "retouch", "paramount", "revenge", "passenger", "reward", "pedigree", "rhythm", "pegasus", "ribcage", "penetrate", "ringbolt", "perceptive", "robust", "performance", "rocker", "pharmacy", "ruffled", "phonetic", "sailboat", "photograph", "sawdust", "pioneer", "scallion", "pocketful", "scenic", "politeness", "scorecard", "positive", "scotland", "potato", "seabird", "processor", "select", "provincial", "sentence", "proximate", "shadow", "puberty", "shamrock", "publisher", "showgirl", "pyramid", "skullcap", "quantity", "skydive", "racketeer", "slingshot", "rebellion", "slowdown", "recipe", "snapline", "recover", "snapshot", "repellent", "snowcap", "replica", "snowslide", "reproduce", "solo", "resistor", "southward", "responsive", "soybean", "retraction", "spaniel", "retrieval", "spearhead", "retrospect", "spellbind", "revenue", "spheroid", "revival", "spigot", "revolver", "spindle", "sandalwood", "spyglass", "sardonic", "stagehand", "saturday", "stagnate", "savagery", "stairway", "scavenger", "standard", "sensation", "stapler", "sociable", "steamship", "souvenir", "sterling", "specialist", "stockman", "speculate", "stopwatch", "stethoscope", "stormy", "stupendous", "sugar", "supportive", "surmount", "surrender", "suspense", "suspicious", "sweatband", "sympathy", "swelter", "tambourine", "tactics", "telephone", "talon", "therapist", "tapeworm", "tobacco", "tempest", "tolerance", "tiger", "tomorrow", "tissue", "torpedo", "tonic", "tradition", "topmost", "travesty", "tracker", "trombonist", "transit", "truncated", "trauma", "typewriter", "treadmill", "ultimate", "trojan", "undaunted", "trouble", "underfoot", "tumor", "unicorn", "tunnel", "unify", "tycoon", "universe", "uncut", "unravel", "unearth", "upcoming", "unwind", "vacancy", "uproot", "vagabond", "upset", "vertigo", "upshot", "virginia", "vapor", "visitor", "village", "vocalist", "virus", "voyager", "vulcan", "warranty", "waffle", "waterloo", "wallet", "whimsical", "watchword", "wichita", "wayside", "wilmington", "willow", "wyoming", "woodlark", "yesteryear", "zulu", "yucatan"]
genKeys(raw_input("Input the password: "), raw_input("Input the checksum: "))
