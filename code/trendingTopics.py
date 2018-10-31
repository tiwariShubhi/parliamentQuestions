# DMG Project - ParliamanetQuestions
# Created by : Shubhi Tiwari
# Date : 31 Oct, 2018
# -------------------------------------------------------------------------------------------------------
# Description : take question_type and finds the most trending topics in the rajyasabha over 10 years
#               across different ministries
#
# Input :
# Output :
#
# --------------------------------------------------------------------------------------------------------

import csv
import nltk
import operator
import string
path = 'D:/m.tech/Sem 3/DMG/Project/parliamentQuestions/rajyasabha/'
fileNamesFile = 'D:/m.tech/Sem 3/DMG/Project/parliamentQuestions/rajyasabha/fileNames.txt'
outFile = 'D:/m.tech/Sem 3/DMG/Project/parliamentQuestions/Results/trendTopics_10years.txt'
stopWords = nltk.corpus.stopwords.words('english') + list(string.punctuation);
fileList = [line.rstrip('\n') for line in open(fileNamesFile)]

# combining for all years and taking ministry wise
quesMinWise = {}
for file in fileList:
    with open(path+file) as csvFile:
        fileData = csv.DictReader(csvFile,)
        for row in fileData:
            #print row['ministry'] ,row['question_title']
            m = row['ministry']
            q = row['question_title']
            if quesMinWise.has_key(m):
                temp = quesMinWise[m]
                temp.append(q)
            else:
                temp = []
                temp.append(q)

            quesMinWise[m] = temp

#print quesMinWise
#print stopWords
c = 0
wordDict = {}
for k,v in quesMinWise.iteritems():
    wordCount = {}
    for ques in v:
        tok = nltk.word_tokenize(ques)
        if '.' in tok:
            tok.remove('.')
        #print tok
        tokens = []
        for t in tok:
            if t.lower() in stopWords:
                continue
            else:
                tokens.append(t)
                if wordCount.has_key(t):
                    wordCount[t] +=1
                else:
                    wordCount[t] = 1

    wordDict[k] = wordCount
fp = open(outFile,'w')
print("-------------------------")
print("--MINISTRY WISE RESULTS---")
for k,v in wordDict.iteritems():
    fp.write(k+'\n')
    print(k)
    #for kk,vv in v.iteritems():
    sorted_topics = sorted(v.items(), key=operator.itemgetter(1),reverse=True)
    print sorted_topics
    fp.write(str(sorted_topics))
    fp.write('\n')
    print('-------------------')
    fp.write('-------------------')
        # tags = nltk.pos_tag(tokens)
        # print tags
        # for t in tags:
        #     if t[1] in ['NN','NNS','NNP','NNPS']:
        #
        #     else:
        #         print 'booyah'
        #         c+=1

print c
fp.close()



