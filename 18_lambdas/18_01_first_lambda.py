'''
Write a lambda function that takes in 3 numbers and returns the sum of the numbers.

'''

numlist = [int(item) for item in (input("Please enter three numbers:").split())]

add = lambda d: sum(numlist)
print (f"The result is {add(numlist)}")