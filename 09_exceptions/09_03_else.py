'''
Write a script that demonstrates a try/except/else.

'''
num1, num2 = input("Please enter two numbers:").split()

try:
    print (int(num1) / int(num2))
except ValueError:
    print ("You didn't enter a number!")
except ZeroDivisionError:
    print ("You can't divide by zero!")
else:
    print("Thanks for playing!")