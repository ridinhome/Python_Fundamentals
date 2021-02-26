'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list= []

for element in starting_list:
    if type(element) is list:
        for sub_element in element:
            flattened_list.append(sub_element)
    else:
        flattened_list.append(sub_element)

print(flattened_list)
