'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = []

for i in range (0,len(list_)):
    if list_[i] not in list_[i+1:len(list_)] and list_[i] not in list_[0:i-1]:
        unique_list.append(list_[i])

print(unique_list)


