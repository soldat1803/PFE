import spacy
from configuration import *
import hashlib
from clozeclass import Cloze

def est_une_cloze(sentence):
    longueur_cloze = NOMBRE_MIN_CHAR_CLOZE <len(sentence) < NOMBRE_MAX_CHAR_CLOZE
    no_links = not (("https://" in sentence) or ("http://" in sentence))
    tokens = sentence.split()
    taille_mots = all(TAILLE_MIN_MOT < len(mot) < TAILLE_MAX_MOT for mot in tokens)
    nombre_mot = NOMBRE_MIN_MOT_CLOZE < len(tokens) < NOMBRE_MAX_MOT_CLOZE
    return (longueur_cloze and no_links and taille_mots and nombre_mot)

def NE_answer_generator(sent):
    return [(e.text, e.start_char - sent.start_char, e.label_) for e in sent.ents]

def NP_answer_generator(sent):
    return [(n_p.text, n_p.start_char - sent.start_char, NOUNPHRASE_LABEL) for n_p in sent.noun_chunks]

def est_une_reponse(sent):
    correct_char_len = TAILLE_MIN_CHAR_ANSWER < len(sent) < TAILLE_MAX_CHAR_ANSWER
    correct_word_len = TAILLE_MIN_WORD_ANSWER < len(sent.split()) < TAILLE_MAX_WORD_ANSWER
    return correct_char_len and correct_word_len

def cloze_id(paragraph_text, sentence_text, answer_text):
    rep = paragraph_text + sentence_text + answer_text
    return hashlib.sha1(rep.encode()).hexdigest()

def mask_answer(text, answer_text, answer_start, answer_type):
    before, after = text[:answer_start], text[answer_start + len(answer_text):]
    return before + CLOZE_MASKS[answer_type] + after

def generate_cloze_fct(text):
    clozes = []
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    for sents in doc.sents:
        is_cloze = est_une_cloze(str(sents))
        if is_cloze:
            answers = NE_answer_generator(sents)
            for answer_text, answer_start, answer_type in answers:
                if est_une_reponse(answer_text):
                    yield Cloze(
                        cloze_id=cloze_id(text, sents.text, answer_text),
                        paragraph = text,
                        source_text = sents.text,
                        source_start = sents.start,
                        cloze_text=mask_answer(sents.text, answer_text, answer_start, answer_type),
                        answer_text=answer_text,
                        answer_start=answer_start,
                        constituency_parse=None,
                        root_label=None,
                        answer_type=answer_type,
                        question_text=None

                    )
    return clozes



                        
