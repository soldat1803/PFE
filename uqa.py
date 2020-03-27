from generate_cloze import *
from cp import *
from noisy_cloze import *
import nltk

files = open("de.txt",'r')
text = files.read()

clozes = generate_cloze_fct(text)
#print(list(clozes))
#short_clozes = get_cloze_p(clozes)
#qc = get_questions_for_clozes(clozes)
k=0
for cloze in clozes:
        k+=1
        if k == 2:
                mot = nltk.word_tokenize(cloze.answer_text)
                cc = shuffle_words(nltk.word_tokenize(cloze.answer_text),params=NoiserParams())
                print(cc)
          
