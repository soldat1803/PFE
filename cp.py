from allennlp.predictors import Predictor
from configuration import *
from allennlp.models.archival import load_archive
from tqdm import tqdm
from nltk import Tree
import attr
import random

def _load_constituency_parser():
    archive = load_archive(CONSTITUENCY_MODEL, cuda_device=CONSTITUENCY_CUDA)
    return Predictor.from_archive(archive, 'constituency-parser')

def get_cloze_p(clozes):
    predictor = _load_constituency_parser()
    jobs = range(0, len(clozes), CONSTITUENCY_BATCH_SIZE)
    desc='Running Constituency Parsing'
    for i in tqdm(jobs, desc=desc, ncols=80) :
        input_batch = clozes[i: i + CONSTITUENCY_BATCH_SIZE]
        output_batch = predictor.predict_batch_json([{'sentence': c.source_text} for c in input_batch])
        for c, t in zip(input_batch, output_batch):
            root = _get_root_type(t['trees'])
            if root in CLOZE_SYNTACTIC_TYPES:
                c_with_parse = attr.evolve(c, constituency_parse=t['trees'], root_label=root)
                yield c_with_parse

def _get_root_type(tree):
    try:
        t = Tree.fromstring(tree)
        label = t.label()
    except:
        label = 'FAIL'
    return label

def get_questions_for_clozes(clozes):
    clozes_with_questions = [attr.evolve(c, question_text=identity_translation(c)) for c in clozes]
    return clozes_with_questions

def identity_translation(cloze):
    repl = _get_wh_word(cloze)
    q = _replace_mask(cloze, repl)
    return _add_q_mark_and_fix_spaces(q)

def _get_wh_word(cloze):
    repl = random.choice(HCTQM[cloze.answer_type])
    return repl

def _replace_mask(cloze, repl):
    return cloze.source_text[:cloze.answer_start] + repl + cloze.source_text[
                                                      cloze.answer_start + len(cloze.answer_text):]

def _add_q_mark_and_fix_spaces(q):
    return q.replace('  ', ' ').rstrip(' ,.') + '?'
def is_appropriate_question(question_text, answer_text, paragraph_text):
    nbr_char_text = len(paragraph_text) <= MAX_TEXT_LEN
    len_word_text = len(paragraph_text.split()) <= MAX_TEXT_WORD
    len_word_correct = all([len(word) <= MAX_TEXT_WORD_LEN for word in paragraph_text.split()] )
    bool_p = nbr_char_text and len_word_text and len_word_correct

    question_char_len = len(question_text) <= MAX_QUESTION_CHAR
    question_word_nbr = len(question_text.split()) <= MAX_QUESTION_WORD
    question_word_len = all([len(w) <= MAX_QUESTION_WORDSIZE for w in question_text.split()])
    bool_q = question_char_len and question_word_nbr and question_word_len

    char_len = TAILLE_MIN_CHAR_ANSWER <= len(answer_text) <= TAILLE_MAX_CHAR_ANSWER
    nbr_word = TAILLE_MIN_WORD_ANSWER <= len(answer_text.split()) <= TAILLE_MAX_WORD_ANSWER
    bool_w = char_len and nbr_word
    return bool_p and bool_q and bool_w




    
