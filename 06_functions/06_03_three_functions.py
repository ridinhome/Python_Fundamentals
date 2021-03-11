'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''

def increment(number):
    result = number + 1
    return (result)

def square(variable):
    square = increment(variable) ** 2
    return (square)

def cubed(integer):
    power_of_three = square (integer) ** 3
    return (power_of_three)

input_num = int(input("Please enter a number"))

x = increment(input_num)
y = square(input_num)
z = cubed(input_num)

print (x,y,z)

