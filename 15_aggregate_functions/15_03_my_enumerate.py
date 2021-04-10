'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''

my_list = ["1", "2", "3"]

def my_enumerate(iterable_to_enumerate):
    counter = 0
    list_to_return = []
    for item in iterable_to_enumerate:
        list_to_return += [(counter,item)]
        counter += 1
    return list_to_return

print (my_enumerate(my_list))
