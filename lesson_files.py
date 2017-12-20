# file_path = r'C:\Users\User\Desktop\test.txt'
# f = open(file_path)
# print(type(f))
#
#
# # write
# f = open(file_path, 'w+')
# for i in range(100):
#     f.write("Hello world %d\n" % i)
# f.close()
#
#
# # read
# f = open(file_path, 'r+')
# line = f.readline()
# while line:
#     print(line)
#     line = f.readline()
# f.close()
#
#

import pprint
import string
import csv

def word_counter(file_path, file_path_stop_words, num_limit=20):

    f = open(file_path)
    content = f.read().lower()
    lst_words = content.split()
    f.close()

    f2 = open(file_path_stop_words)
    content_stop_words = f2.read()
    lst_stop_words = content_stop_words.split()
    f2.close()

    print(len(lst_words))
    print(len(lst_stop_words))

    word_stats = {}
    for word in lst_words:
        if word not in lst_stop_words:
            word = word.strip(string.punctuation)
            if word:
                if word in word_stats:
                    word_stats[word] = word_stats[word] + 1
                else:
                    word_stats[word] = 1

    # pprint.pprint(word_stats)

    for key in sorted(word_stats.keys(),
                      key=lambda key: word_stats[key],
                      reverse=True)[:num_limit]:
        print("%s:\t%d" %(key, word_stats[key]))


word_counter('hhgttg.txt', 'stop_words.txt')


def get_data_from_csv(filename):

    f = open(filename, "r")
    list_dicts = [row for row in csv.DictReader(f)]
    f.close()

    return list_dicts

lst_dicts = get_data_from_csv('cities.csv')
for i, dict in enumerate(lst_dicts):
    print("Entry #", i)
    for k, v in dict.items():
        print("\t%s: %s" % (k, v))