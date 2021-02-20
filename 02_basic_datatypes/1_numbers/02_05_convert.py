'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

value_a = 90
value_b = 11.0

value_a_float = float(value_a)
print (value_a_float)

value_b_float = int(value_b)
print(value_b_float)

value_c = value_a // value_b
print(value_c)

c = input("Enter a value")
b = input("Enter another value")
cd = float(c) * float(b)
print(cd)
