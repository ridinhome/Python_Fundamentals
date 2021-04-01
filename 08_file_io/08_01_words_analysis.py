'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''

my_dict = {}
shortest_list = []
longest_list = []


def shortestword(input_dict):
    '''Function to accept a dictionary, convert it to a tuple, sort it
    and then return the sorted list as well as the length of the longest and shortest words'''
    result_list = []
    for key in input_dict:
        tuple_to_add = key,input_dict[key]
        result_list.append(tuple_to_add)
    new_list = sorted(result_list, key= lambda item:item[1])
    short_length = new_list[0][1]
    list_length = len(new_list)-1
    long_length = new_list[list_length][1]
    return new_list, short_length, long_length

with open("words.txt","r") as fin:
    '''Opens the file, reads the words and then passes them to a dictionary after stripping out new line characters.'''
    for word in fin.readlines():
        word = word.rstrip()
        my_dict[word] = [int(len(word))]

sorted_list,shortest_length,longest_length = shortestword(my_dict)

for key,value in sorted_list:
    '''Creates the list of the shortest words and the longest words.'''
    if value == shortest_length:
        shortest_list.append(key)
    elif value == longest_length:
        longest_list.append(key)

print ("The shortest words are: ",shortest_list)
print ("The longest words are:", longest_list)
print (f"The total number of words are: {len(sorted_list)}")


