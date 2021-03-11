'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''
from statistics import mean

example_list = [1, 2, 3, 4, 5, 6, 7]
min1 = []
max1 = []
average = []
total = []

def stats(num_list):
  min1 = min(num_list)
  max1 = max(num_list)
  average = mean(num_list)
  total = sum(num_list)
  return (min1, max1, average, total)

# call the function below here

min1, max1, average, total = stats(example_list)

print ("The minimum, maximum, average and sum are: ", min1, max1, average, total)


