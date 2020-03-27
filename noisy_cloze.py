from cp import _replace_mask
import nltk
import numpy as np

class NoiserParams(object):
    word_shuffle = 3
    word_dropout = 0.1
    word_blank = 0.2
    blank_word = 'BLANKWORD'

def shuffle_words(tokens,params):
    noise = np.random.uniform(0,params.word_shuffle, size=(len(tokens),))
    return noise

def add_noise(no_mask_tokene,params):
    words = shuffle_words(words, params)
    return words

def get_noisy_cloze(cloze):
    no_mask =  _replace_mask(cloze, '')
    no_mask_tokene = nltk.word_tokenize(no_mask)
    noisy_cloze_tokens = add_noise(no_mask_tokene,params=NoiserParams())
    return no_mask_tokene
