from sklearn.feature_extraction.text import CountVectorizer
import csv
from nltk.stem import WordNetLemmatizer
import string
import nltk
from sklearn.cluster import KMeans
import numpy as np
from scipy import spatial

import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")



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


# def print_top_words(model, feature_names, n_top_words):
#     for topic_idx, topic in enumerate(model.components_):
#         message = "Topic #%d: " % topic_idx
#         message += " ".join([feature_names[i]
#                              for i in topic.argsort()[:-n_top_words - 1:-1]])
#         print(message)
#     print()


def pre_process(data):
    pre_processed_data = []
    wnl = WordNetLemmatizer()

    stop_words = nltk.corpus.stopwords.words('english') + list(string.punctuation)

    # pre-process the data before vectorisation: remove numbers and stopwords; perform lemmatisation and case-folding
    for sample in data:
        sentence = ''
        for word in sample:
            if word.isdigit() is False and word.lower() not in stop_words:
                sentence += wnl.lemmatize(word).lower() + ' '
        pre_processed_data.append(sentence.strip())
    # print pre_processed_data
    # print len(pre_processed_data)
    return pre_processed_data


def vectorise(corpus):
    # tfidf_vectorizer = TfidfVectorizer()
    # tfidf = tfidf_vectorizer.fit_transform(corpus)
    # n_samples, n_features = tfidf.shape
    #
    # print tfidf
    # print '****************', tfidf[0, 0]
    # print n_samples, n_features

    tf_vectorizer = CountVectorizer()
    tf = tf_vectorizer.fit_transform(corpus)
    n_samples, n_features = tf.shape

    # print tf
    # print '*******', tf[0,:]
    # for i in range(0, 7700):
    #     if tf[0, i] != 0:
    #         print tf[0, i]
    print n_samples ,n_features
    print tf_vectorizer.get_feature_names()
    # print tf_vectorizer.get_feature_names()[6239], tf_vectorizer.get_feature_names()[3472], tf_vectorizer.get_feature_names()[7106], tf_vectorizer.get_feature_names()[2250], tf_vectorizer.get_feature_names()[6306], tf_vectorizer.get_feature_names()[6107]
    return tf_vectorizer.get_feature_names(), tf

    # n_components = 10
    # n_top_words = 5
    #
    # tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2,max_features=n_features,)
    # tf = tf_vectorizer.fit_transform(corpus)
    #
    #
    # # Fit the NMF model
    # print("Fitting the NMF model (Frobenius norm) with tf-idf features, "
    #       "n_samples=%d and n_features=%d..."
    #       % (n_samples, n_features))
    # nmf = NMF(n_components=n_components, random_state=1, alpha=.1, l1_ratio=.5).fit(tfidf)
    #
    # tfidf_feature_names = tfidf_vectorizer.get_feature_names()
    # print_top_words(nmf, tfidf_feature_names, n_top_words)
    #
    # # Fit the NMF model
    # print("Fitting the NMF model (generalized Kullback-Leibler divergence) with "
    #       "tf-idf features, n_samples=%d and n_features=%d..."
    #       % (n_samples, n_features))
    #
    # nmf = NMF(n_components=n_components, random_state=1,
    #           beta_loss='kullback-leibler', solver='mu', max_iter=1000, alpha=.1,
    #           l1_ratio=.5).fit(tfidf)
    #
    # print("\nTopics in NMF model (generalized Kullback-Leibler divergence):")
    # tfidf_feature_names = tfidf_vectorizer.get_feature_names()
    # print_top_words(nmf, tfidf_feature_names, n_top_words)


def cluster_data(word_dictionary, data):
    kmeans = KMeans(n_clusters=5, random_state=0).fit(data)
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
        similarity = []
        for sample in cluster:
            sample_arr = sample.toarray()
            x = 1-spatial.distance.cosine(sample_arr, kmeans.cluster_centers_[i])
            similarity.append(x)
        i1 = np.argmax(similarity)
        d1 = cluster[i1]
        similarity[i1] = -1
        i2 = np.argmax(similarity)
        d2 = cluster[i2]
        similarity[i2] = -1
        i3 = np.argmax(similarity)
        d3 = cluster[i3]
        similarity[i3] = -1
        trending_topics_vectors.append(d1)
        trending_topics_vectors.append(d2)
        trending_topics_vectors.append(d3)

    for datapoint in trending_topics_vectors:
        for i in range(0, datapoint.shape[1]):
            if datapoint[0,i] != 0:
                trending_topics.append(word_dictionary[i])

    print 'TRENDING TOPICS ARE:'
    print trending_topics
    return trending_topics






# y,d = read_data('/home/kb/PycharmProjects/DMG_Project2/parliamentQuestions/rajyasabha/rajyasabha_questions_and_answers_2010.csv')
# d = pre_process(d)
# vectorize(d)


print 'read_data called'
year, data = read_data('/home/kb/PycharmProjects/DMG_Project2/parliamentQuestions/rajyasabha/rajyasabha_questions_and_answers_2012.csv')
# print data

print 'pre_process called'
data = pre_process(data)
# print data

print 'vectorise called'
word_dictionary, vectorised_data = vectorise(data)

print 'cluster_data called'
trending_topics = cluster_data(word_dictionary, vectorised_data)
outFile = '/home/kb/PycharmProjects/DMG_Project2/parliamentQuestions/Results/'+'trendingTopics_clustering_sklearn'+str(year)+'.txt'

print 'writing to file'
fp = open(outFile,'w')
fp.write("---TRENDING TOPICS USING CLUSTERING FOR "+str(year)+"---\n")
for topic in trending_topics:
    fp.write(topic+'\n')
fp.close()
