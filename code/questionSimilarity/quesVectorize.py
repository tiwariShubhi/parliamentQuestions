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

lemmatizer = WordNetLemmatizer()
stopWords = nltk.corpus.stopwords.words('english') + list(string.punctuation);
inFile = "D:/m.tech/Sem 3/DMG/Project/parliamentQuestions/rajyasabha/"
questions = {}


