'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

string = input("Please enter a string:")
lower_string = string.lower()
split_string = lower_string.split()
dict_of_words = {item : split_string.count(item) for item in split_string}

Keymax = max(dict_of_words, key=dict_of_words.get)
print (Keymax)

