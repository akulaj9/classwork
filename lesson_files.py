import pprint
import string

file_path = r'C:\Users\User\Desktop\test.txt'
f = open(file_path)
print(type(f))

#write
f = open(file_path, 'w+')
for i in range(100):
    f.write("Hhello world %d\n" % i)
f.close()


#read
f = open(file_path, 'r+')
line = f.readline()
while line:
    print(line)
    line = f.readline()
f.close()

print("******")

def word_counter(file_path, file_path_stop_words, num_limit=20):
    f = open(file_path)
    content = f.read().lower()
    lst_words = content.split()
    f.close()

    f2 = open(file_path_stop_words)
    content_stop_words = f2.read()
    f2.close()

    lst_words = content.split()
    lst_stop_words = content_stop_words.split()

    print(len(lst_words))
    print(len(lst_stop_words))

    word_stars = {}
    for word in lst_words:
        if word not in lst_stop_words:
            word = word.strip(string.punctuation)
            if word:
                if word in word_stars:
                    word_stars[word] = word_stars[word]+ 1
                else:
                    word_stars[word] = 1

    #pprint.pprint(word_stars)


    for key in sorted(word_stars.keys(),
                      key=lambda key: word_stars[key],
                      reverse=True)[:num_limit]:
        print("%s:\t%d" %(key, word_stars[key]))


word_counter('hhgttg.txt', 'stop_words.txt')

