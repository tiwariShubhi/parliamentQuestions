# DMG Project - ParliamanetQuestions
# Created by : Shubhi Tiwari
# Date : 14 Nov, 2018
# -------------------------------------------------------------------------------------------------------
# Description : pre process questions
#
# Input : csv files of Rajsabhya question answer data for past 10 years
# Output :
#
# --------------------------------------------------------------------------------------------------------



import csv
import nltk
import string
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
stopWords = nltk.corpus.stopwords.words('english') + list(string.punctuation);
inFile = "D:/m.tech/Sem 3/DMG/Project/parliamentQuestions/rajyasabha/rajyasabha_questions_and_answers_2009.csv"
questions = {}
with open(inFile) as csvFile:
    fileData = csv.DictReader(csvFile, )
    for row in fileData:
        qNo = row['question']
        qDesc = row['question_description']
        tok = nltk.word_tokenize(qDesc)
        temp = []
        bracketFlag = 0
        for t in tok:
            tt = t.lower()
            if tt=='(':
                bracketFlag = 1
                continue
            elif tt==')':
                bracketFlag =0
                continue
            elif bracketFlag==1:
                continue
            elif tt in stopWords:
                continue
            else:
                print lemmatizer.lemmatize(tt)
                temp.append(lemmatizer.lemmatize(tt))
                # print(tt)

        questions[qNo] = temp

print questions.keys()


