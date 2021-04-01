'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''
while True:
    try:
        value = int(input("Please enter an integer: "))
        print(f"The integer you entered is {value}")
        break
    except ValueError:
        print ("You didn't enter an integer. Please enter an integer: ")

