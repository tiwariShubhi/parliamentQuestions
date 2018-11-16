'''
Steps involved:
1. Vectorize  the question title
2. Perform k-means clustering
3. find trending topics on the basis of centroids
'''

import csv
from nltk.stem import WordNetLemmatizer
import numpy as np
import string
import nltk
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from scipy import spatial


# nltk.download('stopwords')


def read_data(path):
    year = path.split('_')[-1][0:4]
    data = []
    with open(path, 'r') as file:
        row=0
        reader = csv.DictReader(file, delimiter=',')
        for line in reader:
            tuple = line['question_title'].split(' ')
            data.append(tuple)
    return year, data

def vectorise(data):
    pre_processed_data = []
    wnl = WordNetLemmatizer()

    stop_words = nltk.corpus.stopwords.words('english') + list(string.punctuation)

    # pre-process the data before vectorisation: remove numbers and stopwords; perform lemmatisation and case-folding
    for sample in data:
        pre_processed_sample = []
        for word in sample:
            if word.isdigit() is False and word.lower() not in stop_words:
                pre_processed_sample.append(wnl.lemmatize(word).lower())
        pre_processed_data.append(pre_processed_sample)

    # vectorise
    # 1. Create dictionary of all words in all question title
    word_dictionary = []
    for sample in pre_processed_data:
        for word in sample:
            if word in word_dictionary:
                continue
            else:
                word_dictionary.append(word)

    no_of_words = len(word_dictionary)

    # 2. Vectorise each sample
    vectorised_data = []
    for sample in pre_processed_data:
        vector = []
        for word in word_dictionary:
            if word in sample:
                vector.append(sample.count(word))
                sample.remove(word)
            else:
                vector.append(0)
        vectorised_data.append(vector)

    # for vector in vectorised_data:
    #     print vector

    return word_dictionary, vectorised_data


def cluster_data(word_dictionary, data):
    X = np.array(data)
    kmeans = KMeans(n_clusters=5, random_state=0).fit(X)
    # print len(data[0])
    # print len(kmeans.cluster_centers_[0])
    # print kmeans.cluster_centers_[0]

    trending_topics_vectors = []
    trending_topics = []

    for i in range(len(kmeans.cluster_centers_)):
        cluster = []
        for j in range(len(kmeans.labels_)):
            if kmeans.labels_[j] == i:
                cluster.append(data[j])

        '''
        pick 3 nearest data points to the centroid
        '''
        distance = []
        for sample in cluster:
            distance.append(1-spatial.distance.cosine(sample, kmeans.cluster_centers_[i]))
        i1 = np.argmin(distance)
        d1 = cluster[i1]
        distance[i1] = 100
        i2 = np.argmin(distance)
        d2 = cluster[i2]
        distance[i2] = 100
        i3 = np.argmin(distance)
        d3 = cluster[i3]
        distance[i3] = 100
        trending_topics_vectors.append(d1)
        trending_topics_vectors.append(d2)
        trending_topics_vectors.append(d3)

    for datapoint in trending_topics_vectors:
        for i in range(len(datapoint)):
            if datapoint[i] != 0:
                trending_topics.append(word_dictionary[i])

    print 'TRENDING TOPICS ARE:'
    print trending_topics
    return trending_topics


print 'read_data called'
year, data = read_data('/home/kb/PycharmProjects/DMG_Project2/parliamentQuestions/rajyasabha/rajyasabha_questions_and_answers_2010.csv')
print data


print 'vectorise called'
word_dictionary, vectorised_data = vectorise(data)

print 'cluster_data called'
trending_topics = cluster_data(word_dictionary, vectorised_data)
outFile = '/home/kb/PycharmProjects/DMG_Project2/parliamentQuestions/Results/'+'trendingTopics_clustering_'+str(year)+'.txt'

print 'writing to file'
fp = open(outFile,'w')
fp.write("---TRENDING TOPICS USING CLUSTERING FOR "+str(year)+"---\n")
for topic in trending_topics:
    fp.write(topic+'\n')
fp.close()