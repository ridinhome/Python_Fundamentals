'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''

num_str = input ("Please enter a list of numbers:")
split_list = num_str.split()
num_list =[]
tuple_list = []

for i in range (0,len(split_list)):
    num_list.append(int(split_list[i]))

num_list.sort()

if len(num_list) % 2 ==0:
    for i in range (0,len(num_list)-1,2):
        tuple_to_add = (num_list[i],num_list[i+1])
        tuple_list.append(tuple_to_add)

else:
    for i in range (0,len(num_list)-1,2):
        tuple_to_add = (num_list[i],num_list[i+1])
        tuple_list.append(tuple_to_add)
    tuple_to_add = (num_list[len(num_list)-1],0)
    tuple_list.append(tuple_to_add)

print (tuple_list)