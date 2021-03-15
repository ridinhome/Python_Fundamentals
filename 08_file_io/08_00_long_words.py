'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''

words_list = []

with open("words.txt","r") as fin:
    for word in fin.readlines():
        word = word.rstrip()
        if len (word) > 20:
            words_list.append(word)

print(words_list)