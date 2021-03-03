'''
Print out every prime number between 1 and 100.

'''

for num in range (1,100):
    if num == 1 or num == 2:
        print (num)
    else:
        for subnum in range (2,num-1):
            if num % subnum == 0:
                break
            else:
                print(num)










