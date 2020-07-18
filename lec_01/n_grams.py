# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 22:47:47 2020

@author: Sarath C Ani
"""

# Generate the N-grams for the given sentence

import nltk
from nltk.util import ngrams

def extract_ngrams(data, num):
    n_grams = ngrams(nltk.word_tokenize(data), num)
    return [ ' '.join(grams) for grams in n_grams]

text="You overestimates what you can do in a year and underestimates what you can do in 10 years"
grams=2
n_grams=ngrams(nltk.word_tokenize(text) , grams)

print(extract_ngrams(n_grams, grams))
