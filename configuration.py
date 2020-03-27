
# les constants utiliser dans la fonction est_une close de la classe uqa
NOMBRE_MIN_MOT_CLOZE = 5
NOMBRE_MAX_MOT_CLOZE = 40
TAILLE_MIN_MOT = 1
TAILLE_MAX_MOT = 20
NOMBRE_MIN_CHAR_CLOZE = 30     
NOMBRE_MAX_CHAR_CLOZE = 300 

NOUNPHRASE_LABEL = 'NOUNPHRASE'

# les constants utilisé dans la fonction est_une reponse
TAILLE_MIN_CHAR_ANSWER = 3
TAILLE_MAX_CHAR_ANSWER = 50
TAILLE_MIN_WORD_ANSWER = 1
TAILLE_MAX_WORD_ANSWER = 20

CLOZE_MASKS = {
    'PERSON': 'IDENTITYMASK',
    'NORP': 'IDENTITYMASK',
    'FAC': 'PLACEMASK',
    'ORG': 'IDENTITYMASK',
    'GPE': 'PLACEMASK',
    'LOC': 'PLACEMASK',
    'PRODUCT': 'THINGMASK',
    'EVENT': 'THINGMASK',
    'WORKOFART': 'THINGMASK',
    'WORK_OF_ART': 'THINGMASK',
    'LAW': 'THINGMASK',
    'LANGUAGE': 'THINGMASK',
    'DATE': 'TEMPORALMASK',
    'TIME': 'TEMPORALMASK',
    'PERCENT': 'NUMERICMASK',
    'MONEY': 'NUMERICMASK',
    'QUANTITY': 'NUMERICMASK',
    'ORDINAL': 'NUMERICMASK',
    'CARDINAL': 'NUMERICMASK',
    NOUNPHRASE_LABEL: 'NOUNPHRASEMASK'
}

# constituency parser configs:
CONSTITUENCY_MODEL = "https://s3-us-west-2.amazonaws.com/allennlp/models/elmo-constituency-parser-2018.03.14.tar.gz"
CONSTITUENCY_BATCH_SIZE = 32
CONSTITUENCY_CUDA = 0
CLOZE_SYNTACTIC_TYPES = {'S', }

HCTQM = {
    'PERSON': ['Who', ],
    'NORP': ['Who', ],
    'FAC': ['Where', ],
    'ORG': ['Who', ],
    'GPE': ['Where', ],
    'LOC': ['Where', ],
    'PRODUCT': ['What', ],
    'EVENT': ['What', ],
    'WORKOFART': ['What', ],
    'WORK_OF_ART': ['What', ],
    'LAW': ['What', ],
    'LANGUAGE': ['What', ],
    'DATE': ['When', ],
    'TIME': ['When', ],
    'PERCENT': ['How much', 'How many'],
    'MONEY': ['How much', 'How many'],
    'QUANTITY': ['How much', 'How many'],
    'ORDINAL': ['How much', 'How many'],
    'CARDINAL': ['How much', 'How many'],
}

#is_appropriate_question
MAX_TEXT_LEN = 2000
MAX_TEXT_WORD = 400
MAX_TEXT_WORD_LEN = 20
MAX_QUESTION_CHAR = 200
MAX_QUESTION_WORD = 20
MAX_QUESTION_WORDSIZE = 20
