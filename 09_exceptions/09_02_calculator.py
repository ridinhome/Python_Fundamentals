'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''

num1, num2 = input("Please enter two numbers:").split()

try:
    print (int(num1) / int(num2))
except ValueError:
    print ("You didn't enter a number!")
except ZeroDivisionError:
    print ("You can't divide by zero!")
