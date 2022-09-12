# A program script to explore the counting sort algorithm.

# Walkthrough Video Link: https://www.youtube.com/watch?v=BVHP1MUoimc

import time
from random import randint

def counting_sort(array):
	min_value = min(array)
	max_value = max(array)

	count_array = [0 for i in range(min_value, max_value + 1)]
	for value in array:
		index = value - min_value
		count_array[index] += 1

	sorted_array = []
	for index, item in enumerate(count_array):
		if item != 0:
			sorted_array.extend([index + min_value] * item)
	return sorted_array

# The random library is used to create large test arrays.
# array = [3, 1, 7, 7, 9, 2, 11, 12, 4, 2]
array = [randint(0,1000000) for i in range(1000)]
print(f'Unsorted Array: {array[:20]}')

# The time library is used to log a start and end time in seconds.
# This is used to calculate the runtime of the function.
start = time.time()
test = counting_sort(array)
end = time.time()
print(f'Sorted Array: {test[:20]}')
runtime = end - start
print(f'Runtime Counting Sort: {runtime} s.')
