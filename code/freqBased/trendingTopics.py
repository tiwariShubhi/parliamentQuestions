# DMG Project - ParliamanetQuestions
# Created by : Shubhi Tiwari
# Date : 31 Oct, 2018
# -------------------------------------------------------------------------------------------------------
# Description : take question_title and finds the most trending topics in the rajyasabha over 10 years
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
outFile = 'D:/m.tech/Sem 3/DMG/Project/parliamentQuestions/Results/freqOutput/trendTopics2017.txt'
wordCloudTerms = 'D:/m.tech/Sem 3/DMG/Project/parliamentQuestions/Results/topics.txt'

stopWords = nltk.corpus.stopwords.words('english') + list(string.punctuation);
fileList = [line.rstrip('\n') for line in open(fileNamesFile)]
portStem = nltk.stem.PorterStemmer();
# non ministry wise / overall
quesMinWise = []
words= []
for file in fileList:
    with open(path+file) as csvFile:
        fileData = csv.DictReader(csvFile,)
        for row in fileData:
            # print row['ministry'] ,row['question_title']
            m = row['ministry']
            q = row['question_title']
            quesMinWise.append(q)

print('read all files')

wordDict = {}
for v in quesMinWise:
    #wordCount = {}
    tok = nltk.word_tokenize(v)
    if '.' in tok:
        tok.remove('.')
    #print tok
    #tokens = []
    for t in tok:
        tt = t.lower()
        if tt in stopWords:
            continue
        else:
            #tokens.append(tt)
            tt = portStem.stem(tt)
            words.append(tt)
            if wordDict.has_key(tt):
                wordDict[tt] +=1
            else:
                wordDict[tt] = 1
    print 'done'
sorted_topics = sorted(wordDict.items(), key=operator.itemgetter(1),reverse=True)
fp = open(outFile,'w')
print('----------------------------------')
print('----------------------------------')
for vv in sorted_topics:
    fp.write(vv[0]+","+str(vv[1])+"\n")

fp.close()
#
# fp = open(wordCloudTerms,'w')
# for w in words:
#     fp.write(w+" ")
# fp.close()
#
# fp = open(wordCloudTerms).read()
# print "making cloud..."
# # wc = wordcloud.WordCloud(collocations=False,stopwords=wordcloud.STOPWORDS,background_color='white',width=9000,height=4000).generate(fp)
# #
# # plt.imshow(wc)
# # plt.axis('off')
# # plt.show()
#
#
# # generating a histogram of trending words
# n = 20
# counts = dict(Counter(words).most_common(n))
# print len(words)
# print counts
# # for k,v in counts.iteritems():
# #     counts[k] = math.log10(v)
#
# print "counter done"
# labels, values = zip(*counts.items())
#
# # sort your values in descending order
# indSort = np.argsort(values)[::-1]
# print "sorted"
#
# # rearrange your data
# labels = np.array(labels)[indSort]
# values = np.array(values)[indSort]
#
# indexes = np.arange(len(labels))
#
# bar_width = 0.35
#
# print "plotting"
# plt.bar(indexes, values)
#
# # add labels
# plt.xticks(indexes + bar_width, labels)
# plt.ylabel("Word Freqency")
# plt.xlabel("Top 20 words")
# plt.show()
#
#
# # combining for all years and taking ministry wise
# quesMinWise = {}
# for file in fileList:
#     with open(path+file) as csvFile:
#         fileData = csv.DictReader(csvFile,)
#         for row in fileData:
#             #print row['ministry'] ,row['question_title']
#             m = row['ministry']
#             q = row['question_title']
#             if quesMinWise.has_key(m):
#                 temp = quesMinWise[m]
#                 temp.append(q)
#             else:
#                 temp = []
#                 temp.append(q)
#
#             quesMinWise[m] = temp
#
# #print quesMinWise
# #print stopWords
# c = 0
# wordDict = {}
# for k,v in quesMinWise.iteritems():
#     wordCount = {}
#     for ques in v:
#         tok = nltk.word_tokenize(ques)
#         if '.' in tok:
#             tok.remove('.')
#         #print tok
#         tokens = []
#         for t in tok:
#             if t.lower() in stopWords:
#                 continue
#             else:
#                 tokens.append(t)
#                 if wordCount.has_key(t):
#                     wordCount[t] +=1
#                 else:
#                     wordCount[t] = 1
#
#     wordDict[k] = wordCount
# fp = open(outFile,'w')
# print("-------------------------")
# print("--MINISTRY WISE RESULTS---")
# for k,v in wordDict.iteritems():
#     fp.write(k+'\n')
#     print(k)
#     #for kk,vv in v.iteritems():
#     sorted_topics = sorted(v.items(), key=operator.itemgetter(1),reverse=True)
#     print sorted_topics
#     fp.write(str(sorted_topics))
#     fp.write('\n')
#     print('-------------------')
#     fp.write('-------------------')
#         # tags = nltk.pos_tag(tokens)
#         # print tags
#         # for t in tags:
#         #     if t[1] in ['NN','NNS','NNP','NNPS']:
#         #
#         #     else:
#         #         print 'booyah'
#         #         c+=1
#
# print c
# fp.close()
#
#
#
