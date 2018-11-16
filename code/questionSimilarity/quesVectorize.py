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
from sklearn.feature_extraction.text import TfidfVectorizer


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
            t2 += lemmatizer.lemmatize(tt)
            # print(tt)
    return t2



lemmatizer = WordNetLemmatizer()
stopWords = nltk.corpus.stopwords.words('english') + list(string.punctuation);
inFile = "D:/m.tech/Sem 3/DMG/Project/parliamentQuestions/rajyasabha/"
questions = {}
path = 'D:/m.tech/Sem 3/DMG/Project/parliamentQuestions/rajyasabha/similarity/data_development_2010_to_2012.json'
fileName = ''
questions = {}
with open(path,'r') as fileJSON:
    questions = json.load(fileJSON,encoding='latin-1')

allData = []


for k,v in questions.iteritems():
    currYear = questions[k]
    for kk,vv in currYear.iteritems():
        temp = preProcess(vv)
        allData.append(temp)
        currYear[kk] = temp
    questions[k] = currYear

# print allData

vectorizer = TfidfVectorizer()
quesVec = vectorizer.fit_transform(allData)
print quesVec
