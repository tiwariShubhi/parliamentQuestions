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
from sklearn.metrics.pairwise import linear_kernel
from scipy.sparse import csr_matrix
import numpy as np

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
path = 'D:/m.tech/Sem 3/DMG/Project/parliamentQuestions/rajyasabha/similarity/data_CIVIL AVIATION_2010_to_2012.json'
years = ['2010','2011','2012']

fileName = ''
questions = {}
with open(path,'r') as fileJSON:
    questions = json.load(fileJSON,encoding='latin-1')

allData = []

counts = []
#for k,v in questions.iteritems():
for y in years:
    currYear = questions[y]
    c = 0
    for kk,vv in currYear.iteritems():
        temp = preProcess(vv)
        allData.append(temp)
        currYear[kk] = temp
        c += 1
    questions[y] = currYear
    counts.append(c)
# print allData

vectorizer = TfidfVectorizer()
quesVec = vectorizer.fit_transform(allData)

x = csr_matrix.todense(quesVec)
vecs = []
# print x[:counts[0]]
start = 0
for c in counts:
    vecs.append(x[start:start+c,:])
    start = c

sims = []
for i in range(len(counts)-1):
    xMat = vecs[i]
    yMat = vecs[i+1]
    sim = findSimilarity(xMat,yMat)
    #print sim
    print np.sum(sim)
    print(counts[i]*counts[i+1])
    s = np.sum(sim)/(counts[i]*counts[i+1])
    print s
    sims.append(s)
    # for x in xMat:

# print x

for i in range(0,len(years)-1):
    print("Similarity between "+ years[i]+" and "+ years[i+1]+ " is "+ str(sims[i]))