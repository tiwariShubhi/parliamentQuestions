# DMG Project - ParliamanetQuestions
# Created by : Shubhi Tiwari
# Date : 31 Oct, 2018
# -------------------------------------------------------------------------------------------------------
# Description : take ministries common over 10 years
#
# Input : Rajsabhya question answer data for past 10 years
# Output : wordcloud and graph of most trending topics ob=ver the past 10 years
#
# --------------------------------------------------------------------------------------------------------
from collections import Counter
import csv
import nltk
import operator
import string
import wordcloud
import numpy as np
from scipy.misc import imread
import matplotlib.pyplot as plt

path = 'D:/m.tech/Sem 3/DMG/Project/parliamentQuestions/rajyasabha/'
fileNamesFile = 'D:/m.tech/Sem 3/DMG/Project/parliamentQuestions/rajyasabha/fileN.txt'
outFile = 'D:/m.tech/Sem 3/DMG/Project/parliamentQuestions/Results/ministryList5Year.txt'


#stopWords = nltk.corpus.stopwords.words('english') + list(string.punctuation);
fileList = [line.rstrip('\n') for line in open(fileNamesFile)]
#portStem = nltk.stem.PorterStemmer();
# non ministry wise / overall
quesMinWise = []
words= []
ministry = set()
firstFlag = 0
for file in fileList:
    with open(path+file) as csvFile:
        tempMin = set()
        fileData = csv.DictReader(csvFile,)
        for row in fileData:
            # print row['ministry'] ,row['question_title']
            m = row['ministry']
            tempMin.add(m)
        if firstFlag == 0:
            ministry = tempMin
            firstFlag = 1
        else:
            ministry = ministry.intersection(tempMin)


print ministry
print len(ministry)
print('read all files')
fp = open(outFile,'w')
print('----------------------------------')
print('----------------------------------')
for vv in ministry:
    fp.write(vv+"\n")

fp.close()


