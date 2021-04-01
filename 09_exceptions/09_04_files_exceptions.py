'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

'''

import os
path = ("/Users/ridinhome/Documents/CodingNomads/labs/09_exceptions/books/")
war_and_peace = []
crime_and_punishment = ("")
first_letter = {}
os.chdir(path)
file_list = ["war_and_peace.txt","crime_and_punishment.txt","pride_and_prejudice.txt"]

###,

# with open("war_and_peace.txt","r") as tolstoy:
#     for item in tolstoy:
#         war_and_peace.append(item)
#
# print (war_and_peace)

# with open("crime_and_punishment.txt","w") as dostoyevsky:
#     dostoyevsky.write(crime_and_punishment)

for item in file_list:
    with open(item,"r") as book:
        lines = book.readline()
        first_letter[item] = lines[0][0]

for value in first_letter.values():
    print (value)





