'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''

#initializing list
num_list = []

for i in range (0,10):
    num_list.append(input("Please enter a number :"))

for i in range (1,11,2):
    print (num_list[i])

for i in range (8,-1,-2):
    print (num_list[i])



