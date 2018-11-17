# DMG Project - ParliamanetQuestions
# Created by : Shubhi Tiwari
# Date : 14 Nov, 2018
# -------------------------------------------------------------------------------------------------------
# Description : pre process questions and vectorize them
#
# Input : json file of selected topic for a duration of years
# Output :
#
# --------------------------------------------------------------------------------------------------------

import nltk
import string
from nltk.stem import WordNetLemmatizer
import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from scipy.sparse import csr_matrix
import numpy as np
import csv

def preProcess(qDesc):
    tok = nltk.word_tokenize(qDesc)
    temp = []
    t2 = ""
    bracketFlag = 0
    for t in tok:
        tt = t.lower()
        if tt == '(':
            bracketFlag = 1
            continue
        elif tt == ')':
            bracketFlag = 0
            continue
        elif bracketFlag == 1:
            continue
        elif tt in stopWords:
            continue
        else:
            # print lemmatizer.lemmatize(tt)
            temp.append(lemmatizer.lemmatize(tt))
            t2 = t2 + lemmatizer.lemmatize(tt) + " "
            # print(tt)
    return t2

def findSimilarity(x,y):
    cosSim  = linear_kernel(x, y).flatten()
    return  cosSim


lemmatizer = WordNetLemmatizer()
stopWords = nltk.corpus.stopwords.words('english') + list(string.punctuation);
inFile = "D:/m.tech/Sem 3/DMG/Project/parliamentQuestions/rajyasabha/"
questions = {}
path = 'D:/m.tech/Sem 3/DMG/Project/parliamentQuestions/rajyasabha/similarity/all3/'
outfilePath = 'D:/m.tech/Sem 3/DMG/Project/parliamentQuestions/rajyasabha/similarity/outSim5YearBiGram.csv'
# years = ['2009','2010','2011','2012','2013','2014','2015','2016','2017']
years = ['2013','2014','2015','2016','2017']
fileName = ''
questions = {}

fileList = os.listdir(path)
