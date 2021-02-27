'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

inputstr = input("Please enter a string:")
strlist = inputstr.split()
substr = []
results_list =[]

for element in strlist:
    results_list.append(list(element))

print (results_list)




