# A program script to explore the bubble sort algorithm.

import time
from random import randint

def bubble_sort(array):
	# Create a flag to tell us when the sort is complete.
	sort = False
	cycle = 0
	while sort == False:
		sort = True
		# Iterate through the list of numbers and compare pairs.
		for i in range(0, len(array) - 1 - cycle):
			# If a value is larger than its neighbour we switch them.
			if array[i] < array[i + 1]:
				array[i], array[i + 1] = array[i + 1], array[i]
				sort = False
		cycle += 1

	return array

# The random library is used to create large test arrays.
# array = [4, 6, 2, 9, 8, 7, 1, 2, 4, 8]
array = [randint(0, 10) for i in range(100)]
print(f'Unsorted array: {array[:10]}')

# The time library is used to log a start and end time in seconds.
# This is used to calculate the runtime of the function.
start = time.time()
test = bubble_sort(array)
end = time.time()
runtime = end - start

print(f'Sorted array: {test[:10]}')
print(f'Runtime: {runtime} s.')
