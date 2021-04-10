'''
Write a simple aggregate function, sum(), that takes a list a returns the sum.

'''

list_of_numbers = [1,2,3]

def sum_of_numbers(numlist):
    value = 0
    for item in numlist:
        value += item
        # print (item)
    return (value)

total = sum_of_numbers(list_of_numbers)

print (total)
