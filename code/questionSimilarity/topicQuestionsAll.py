# DMG Project - ParliamanetQuestions
# Created by : Shubhi Tiwari
# Date : 14 Nov, 2018
# -------------------------------------------------------------------------------------------------------
# Description : fetch questions for each ministry and save files
#
# Input :
# Output :
#
# --------------------------------------------------------------------------------------------------------

import csv
import json
import re

path = 'D:/m.tech/Sem 3/DMG/Project/parliamentQuestions/rajyasabha/'
# file containing name of files to be processed
# fileNamesFile = path + 'qSimFileNames.txt'
fileNamesFile = path + 'fileN.txt'
ministryFile = 'D:/m.tech/Sem 3/DMG/Project/parliamentQuestions/Results/ministryList5Year.txt'
topic = 'project'
ministryList = [line.rstrip('\n') for line in open(ministryFile)]
pre = 'rajyasabha_questions_and_answers_'
yearLen = 4
first = ''
last = ''
firstFlag =0
fileList = [line.rstrip('\n') for line in open(fileNamesFile)]

for ministry in ministryList:
    questions = {}
    for file in fileList:
        with open(path + file) as csvFile:
            fileData = csv.DictReader(csvFile, )
            currYearQues = {}
            c = 0
            for row in fileData:
                quesTitle = row['question_title']
                desc = row['question_description']
                qNo = row['question']
                min = row['ministry']
                if min == ministry:
                # if re.search(topic,quesTitle,re.IGNORECASE):
                    # print "true"
                    currYearQues[qNo] = desc
                    c+=1

            year = file[len(pre):len(pre)+yearLen]
            questions[year] = currYearQues
            if firstFlag == 0:
                first = year
                firstFlag = 1
            last = year
            print(year + " "+ str(c))
    with open(path+'similarity/all3/data_'+ministry+'_'+first+'_to_'+last+'.json','w') as jsonfile:
        json.dump(questions, jsonfile,encoding='latin-1')

