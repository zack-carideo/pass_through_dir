# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:15:28 2019

@author: zjc10
"""
import string
import re 

def clean_sentence(sentence,PUNCTUATION=string.punctuation+"\\\\",stemmer = None, lower=False,stopwords = None):
    sentence = sentence.encode('ascii',errors = 'ignore').decode()
    sentence=re.sub(f'[{PUNCTUATION}]',' ',sentence)
    sentence = re.sub(' {2,}',' ', sentence)
    if lower:
        sentence= sentence.lower().strip()
    else:
        sentence= sentence.strip()
    
    if stopwords: 
        sentence = ' '.join([word for word in sentence.split() if word not in stopwords])
    
    if stemmer: 
        sentence = ' '.join([stemmer.stem(word) for word in sentence.split()])
    return sentence 

    