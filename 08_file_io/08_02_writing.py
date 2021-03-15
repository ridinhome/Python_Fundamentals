'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

my_list = []

with open("words.txt","r") as fin:
    for word in fin.readlines():
        word = word.rstrip()
        my_list.append(word)

reversed_list = reversed(my_list)

with open("words_reverse.txt","w") as fout:
    for item in reversed_list:
        fout.write('%s\n' % item)

