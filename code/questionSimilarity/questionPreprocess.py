# DMG Project - ParliamanetQuestions
# Created by : Shubhi Tiwari
# Date : 14 Nov, 2018
# -------------------------------------------------------------------------------------------------------
# Description : pre process questions
#
# Input : Rajsabhya question answer data for past 10 years
# Output :
#
# --------------------------------------------------------------------------------------------------------


import nltk
import spacy
import csv

lemmatizer = spacy.load("en_core_web_sm")
inFile = ""
questions = {}
with open(inFile) as csvFile:
    fileData = csv.DictReader(csvFile, )
    for row in fileData:
        qNo = row['question_no']
        qDesc = row['question_description']
        


