# A program script to explore the radix sort algorithm.

# Walkthrough Video Link: https://www.youtube.com/watch?v=6iYS3VfZE-o

import math
import time
from random import randint

def count_sort_10(array, i):
	base_10 = 10 ** i
	new_array = [[] for x in range(0, 10)]
	for value in array:
		index = value // base_10
		new_array[index % 10].append(value)

	output = []
	for item in new_array:
		output.extend(item)
	return output

def radix_sort(array):
	max_value = max(array)
	max_i = int(math.log(max_value, 10))

	for i in range(0, max_i + 1):
		array = count_sort_10(array, i)
	return array

# The random library is used to create large test arrays.
# array = [42, 96, 72, 1002, 293, 324, 323, 939]
array = [randint(0,1000000) for i in range(100000)]
print(f'Unsorted Array: {array[0:10]}')

# The time library is used to log a start and end time in seconds.
# This is used to calculate the runtime of the function.
start = time.time()
test = radix_sort(array)
end = time.time()
runtime = end - start

print(f'Sorted Array: {test[0:10]}')
print(f'Runtime: {runtime} s.')
