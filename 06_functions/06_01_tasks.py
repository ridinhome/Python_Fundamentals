'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

# print your new variables to display the results

def four_or_seven (number):
    if number % 4 == 0 or number % 7 == 0:
        return True
    else:
        return False

def four_and_seven (number):
    if number % 4 == 0 and number % 7 ==0:
        return True
    else:
        return False

num = int(input("Enter a number between 1 adn 1,000,000,000: "))

div_by_or = four_or_seven(num)

div_by_both = four_and_seven(num)

print (num, " is divisible by either:", div_by_or)

print (num, " is divisible by both:", div_by_both)

