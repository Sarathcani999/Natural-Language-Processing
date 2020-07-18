"""
Created on Sat Jul 18 22:08:02 2020

@author: Sarath C Ani
"""

import nltk

# stopwords
# corpus is nothing but collection of text
from nltk.corpus import stopwords
words=stopwords.words('english')

# Tokenizing - breaks when it finds a space
# punctuations are taken as tokens
example_sent = "This is a sample sentence, showing off the stop words filtration. Hi how'you sangeetha's"
from nltk.tokenize import word_tokenize,sent_tokenize
word_tokens = word_tokenize(example_sent)
sent_tokens = sent_tokenize(example_sent)

# Whitespace tokenizer
# Treebankword tokenizer
# WordPunct tokenizer

# Filtering
filtered_sentence = [w for w in word_tokens if w not in words]

# Stemming
# PorterStemmer
# LancasterStemmer
# SnowballStemmer

# Lemmatizer(7)
# Wordnet
# Spacy
# TextBlob
# CLiPS Pattern
# Stanford CoreNLP
# Gensim 
# TreeTagger