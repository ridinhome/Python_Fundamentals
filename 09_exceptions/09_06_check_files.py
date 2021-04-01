'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

file_name = 'integers.txt'
# my_numbers = ["aaa","bbb"]
my_numbers = ["aaa"]

while True:
    try:
        with open(file_name, "r") as integers:
            for numbers in integers.readlines():
                numbers = numbers.rstrip()
                my_numbers.append(numbers)
        print(f"The calculation is {int(my_numbers[0]) / 5}")
        break
    except (ValueError, TypeError):
        if my_numbers[0].isalpha() == True:
            for item in my_numbers:
                if item.isalpha() == True:
                    continue
                else:
                    print(f"The calcualtion is {int(item) / 5}")
                    break
        else:
            print (f"The calculation is {int(my_numbers[0] / 5)}")
        break
    except IOError:
        print ("Incorrect file name")
        break