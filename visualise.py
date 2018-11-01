import numpy
import csv
import pandas as pd
import matplotlib.pyplot as plt

'''
1. For a year, #questions asked monthly: divided into ministries
2. Total questions asked by each ministry across all years
3. 
'''


def read_data(path):
    data = pd.read_csv(path)
    df = pd.DataFrame(data)
    print 'Headers are:', list(df)
    return df

# read_data('/home/kb/PycharmProjects/DMG_Project/rajyasabha/rajyasabha_questions_and_answers_2009.csv')



def get_ministries(path, all_ministries):
    df = read_data(path)
    year = path.split('_')[-1][0:4]
    for ministry in set(df['ministry']):
        if ministry in all_ministries.keys():
            all_ministries[ministry].append(year)
        else:
            all_ministries[ministry] = [year]
    return all_ministries


def ministry_wise_stats(path):
    year = path.split('_')[-1][0:4]
    df = read_data(path)
    stat = df.groupby('ministry').size()
    print stat
    ministries = stat.index
    no_of_questions = []
    for count in stat:
        no_of_questions.append(count)
    plot(ministries, no_of_questions, year)



def monthly_ministry_wise_stats_yearly(path):
    year = path.split('_')[-1][0:4]
    df = read_data(path)
    df['answer_month'] = 12
    for index, row in df.iterrows():
        df.loc[index, 'answer_month'] = row['answer_date'].split('.')[1]
    stat1 = df.groupby('answer_month').size()
    # print stat1
    months = stat1.index
    no_of_questions = []
    for count in stat1:
        no_of_questions.append(count)
    # plot(months, no_of_questions)

    stat2 = df.groupby(['ministry', 'answer_month'])

    month_ministry_questionscount = {}
    no_of_months = 12
    all_ministries = set(df['ministry'])
    no_of_ministries = len(all_ministries)
    ministry_indices = {}

    i=0
    for ministry in all_ministries:
        ministry_indices[ministry] = i
        i += 1

    for month in range(0, no_of_months):
        month_ministry_questionscount[month] = [0]*no_of_ministries

    for ind, sub_df in stat2:
        ministry = list(ind)[0]
        month = list(ind)[1]
        print ministry, month, sub_df.size
        month_ministry_questionscount[int(month)-1][ministry_indices[ministry]] = sub_df.size

    index = numpy.arange(no_of_ministries)
    width = 0.40
    colors = ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11']
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    plt.bar(index, month_ministry_questionscount[0], width, label=months[0])
    for i in range(1, no_of_months):
        print 'plotting for ',i
        plt.bar(index, month_ministry_questionscount[i][:], width, bottom=month_ministry_questionscount[i-1][:], label=months[i])

    print month_ministry_questionscount[01][ministry_indices['HUMAN RESOURCE DEVELOPMENT']]
    print month_ministry_questionscount[02][ministry_indices['HUMAN RESOURCE DEVELOPMENT']]
    print month_ministry_questionscount[03][ministry_indices['HUMAN RESOURCE DEVELOPMENT']]
    print month_ministry_questionscount[06][ministry_indices['HUMAN RESOURCE DEVELOPMENT']]
    print month_ministry_questionscount[07][ministry_indices['HUMAN RESOURCE DEVELOPMENT']]



    plt.ylabel('No. of questions')
    plt.yticks(numpy.arange(0, 3000, 50), fontsize=5)
    plt.title('Ministry-month-wise stats for '+str(year))
    all_ministry_names = ['']*no_of_ministries
    for key in ministry_indices.keys():
        all_ministry_names[ministry_indices[key]] = key


    plt.xticks(index, all_ministry_names, rotation=270, fontsize=5)
    # TODO
    # Write legend
    # plt.legend(())
    legend = plt.legend(loc='upper right', shadow=True, fontsize=5)

    # Put a nicer background color on the legend.
    legend.get_frame()

    plt.show()




    # no_of_ministries = len(set(df['ministry']))
    # for ministry in set(df['ministry']):
    #     ministry_month_wise_count[ministry] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #
    # print stat2
    #
    # for ind, sub_df in stat2:
    #     ministry = list(ind)[0]
    #     month = list(ind)[1]
    #     print sub_df.size, ministry, month
    #     ministry_month_wise_count[ministry][int(month)] = sub_df.size
    #
    # print ministry_month_wise_count
    # print 'Number of ministries', no_of_ministries
    #
    # # plot_data = []
    # N = 12
    # index = numpy.arange(N)
    # width = 0.35
    # ministries = ministry_month_wise_count.keys()
    # plots = []
    # plots.append(plt.bar(index, ministry_month_wise_count[ministries[0]][1:], width, label=ministries[0]))
    # for i in range(1, no_of_ministries):
    #     plots.append(plt.bar(index, ministry_month_wise_count[ministries[i]][1:], width,
    #                          bottom=ministry_month_wise_count[ministries[i - 1]][1:], label=ministries[i]))
    # plt.ylabel('No. of questions')
    # plt.title('Ministry-month-wise stats')
    # plt.xticks(index, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    # # TODO
    # # Write legend
    # # plt.legend(())
    # legend = plt.legend(loc='upper right', shadow=True, fontsize=5)
    #
    # # Put a nicer background color on the legend.
    # legend.get_frame()
    #
    # plt.show()


def monthly_stats_yearwise(path):

    df = read_data(path)
    df['answer_month'] = 12
    for index, row in df.iterrows():
        df.loc[index, 'answer_month'] = row['answer_date'].split('.')[1]
    stat1 = df.groupby('answer_month').size()
    # print stat1
    months = stat1.index
    no_of_questions = []
    for count in stat1:
        no_of_questions.append(count)
    # plot(months, no_of_questions)

    stat2 = df.groupby(['ministry', 'answer_month'])

    ministry_month_wise_count = {}
    no_of_ministries = len(set(df['ministry']))
    for ministry in set(df['ministry']):
        ministry_month_wise_count[ministry] = [0,0,0,0,0,0,0,0,0,0,0,0,0]

    print stat2

    for ind, sub_df in stat2:
        ministry = list(ind)[0]
        month = list(ind)[1]
        print sub_df.size, ministry, month
        ministry_month_wise_count[ministry][int(month)] = sub_df.size

    print ministry_month_wise_count
    print 'Number of ministries', no_of_ministries


    # plot_data = []
    N = 12
    index = numpy.arange(N)
    width = 0.35
    ministries = ministry_month_wise_count.keys()
    plots = []
    plots.append(plt.bar(index, ministry_month_wise_count[ministries[0]][1:], width, label=ministries[0]))
    for i in range(1, no_of_ministries):
        plots.append(plt.bar(index, ministry_month_wise_count[ministries[i]][1:], width, bottom=ministry_month_wise_count[ministries[i-1]][1:], label=ministries[i]))
    plt.ylabel('No. of questions')
    plt.title('Ministry-month-wise stats')
    plt.xticks(index, [1,2,3,4,5,6,7,8,9,10,11,12])
    #TODO
    #Write legend
    # plt.legend(())
    legend = plt.legend(loc='upper right', shadow=True, fontsize=5)

    # Put a nicer background color on the legend.
    legend.get_frame()

    plt.show()



    # print stat2
    # print stat2.index
    # print 'stat2.index[0]', stat2.index[0]          #prints: stat2.index[0] ('AGRICULTURE', 12)
    # print 'stat2.index[0][0]', stat2.index[0][0]    #prints: stat2.index[0][0] AGRICULTURE
    # print 'stat2.index[0][0][0]', stat2.index[0][0][0]    #prints: stat2.index[0][0] AGRICULTURE

    # ministry_wise_count = {}
    # no_of_ministries = len(set(df['ministry']))
    # for ministry in set(df['ministry']):
    #     ministry_wise_count[ministry] = 0
    #
    # print 'PRINTING SUB-DF'
    # for sub_df in stat2:
    #     print sub_df
    #     break
    # print 'stat2[\'AGRICULTURE\']', stat2['AGRICULTURE']
    # for i in range(0, no_of_ministries):
    #     ministry_wise_count[stat2.index[i][0]] =
    #
    # return ministry_wise_count

    # N = 5
    # menMeans = (20, 35, 30, 35, 27)
    # womenMeans = (25, 32, 34, 20, 25)
    # menStd = (2, 3, 4, 1, 2)
    # womenStd = (3, 5, 2, 3, 3)
    # ind = np.arange(N)  # the x locations for the groups
    # width = 0.35  # the width of the bars: can also be len(x) sequence
    #
    # p1 = plt.bar(ind, menMeans, width, yerr=menStd)
    # p2 = plt.bar(ind, womenMeans, width,
    #              bottom=menMeans, yerr=womenStd)
    #
    # plt.ylabel('Scores')
    # plt.title('Scores by group and gender')
    # plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
    # plt.yticks(np.arange(0, 81, 10))
    # plt.legend((p1[0], p2[0]), ('Men', 'Women'))
    #
    # plt.show()



def whole_stats(paths):
    all_ministries = {}
    all_ministries = get_ministries(paths[0], all_ministries)
    all_ministries = get_ministries(paths[1], all_ministries)

    list_of_ministries = list(all_ministries.keys())

    all_data_stats = []
    for path in paths:
        all_data_stats.append(monthly_stats_yearwise(path))
    N = len(all_data_stats)
    index = numpy.arange(N)
    width = 0.35
    plt.bar(index, all_data_stats[0], width)
    for i in range(1, len(all_data_stats)):
        plt.bar(index, all_data_stats[i], width, bottom=all_data_stats[i-1])
    plt.ylabel('No. of Questions')
    plt.title('Stats for Whole Data')
    plt.xticks(index, ('2009', '2010'))     #, '2011', '2012', '2013', '2014', '2015', '2016', '2017'
    plt.show()

def plot(ministries, count, year):
    labels = numpy.arange(len(ministries))
    plt.barh(labels, count)

    plt.ylabel('Ministries')
    plt.xlabel('No of Questions')
    plt.yticks(labels, ministries, fontsize=5)
    plt.title('No of Questions wrt Ministries for year '+str(year))
plt.show()

path_09 = '/home/kb/PycharmProjects/DMG_Project/rajyasabha/rajyasabha_questions_and_answers_2009.csv'
path_10 = '/home/kb/PycharmProjects/DMG_Project/rajyasabha/rajyasabha_questions_and_answers_2010.csv'
path_11 = '/home/kb/PycharmProjects/DMG_Project/rajyasabha/rajyasabha_questions_and_answers_2011.csv'
path_16 = '/home/kb/PycharmProjects/DMG_Project/rajyasabha/rajyasabha_questions_and_answers_2016.csv'
path_17 = '/home/kb/PycharmProjects/DMG_Project/rajyasabha/rajyasabha_questions_and_answers_2017.csv'

paths = [path_09, path_10]
# monthly_stats(path)
# whole_stats(paths)
# get_ministries(path_09)
monthly_ministry_wise_stats_yearly(path_17)