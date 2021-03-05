'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

number = int(input("Please enter a number between 0 and 1,000,000,000:"))
check = 0

while check != number:
    check += 1

print (check)
