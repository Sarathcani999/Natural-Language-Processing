# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 22:36:36 2020

@author: Sarath C Ani
"""

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
words=["running" , "ran" , "ate" , "went"]
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]