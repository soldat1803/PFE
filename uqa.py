import spacy
from configuration import *
def est_une_cloze(sentence):
    longueur_cloze = NOMBRE_MIN_CHAR_CLOZE <len(sentence) < NOMBRE_MAX_CHAR_CLOZE
    no_links = not (("https://" in sentence) or ("http://" in sentence))
    tokens = sentence.split()
    taille_mots = all(TAILLE_MIN_MOT < len(mot) < TAILLE_MAX_MOT for mot in tokens)
    nombre_mot = NOMBRE_MIN_MOT_CLOZE < len(tokens) < NOMBRE_MAX_MOT_CLOZE
    return (longueur_cloze and no_links and taille_mots and nombre_mot)


files = open("de.txt",'r')
text = files.read()
clozes = []
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
for sents in doc.sents:
    print(sents," bool ", est_une_cloze(str(sents)) ,"\n\n\n")
    