# A program script to explore the quick sort algorithm.

# Walkthrough Video Link: https://www.youtube.com/watch?v=ieXu7YD_m6o

import time
from random import randint

def quick_sort(array):
	if len(array) <= 1:
		return array

	pivot_index = randint(0, len(array) - 1)
	pivot = array[pivot_index]

	lesser, same, greater = [], [], []

	for element in array:
		if element == pivot:
			same.append(element)
		elif element < pivot:
			lesser.append(element)
		elif element > pivot:
			greater.append(element)

	return quick_sort(lesser) + same + quick_sort(greater)

# The random library is used to create large test arrays.
# array = [4, 10, 8, 6, 12, 3, 5, 9, 1, 3]
array = [randint(0, 100) for i in range(100000)]

# The time library is used to log a start and end time in seconds.
# This is used to calculate the runtime of the function.
start = time.time()
test = quick_sort(array)
end = time.time()
runtime = end - start

print(f'Sorted List: {test[:20]}')
print(f'Runtime: {runtime} s.')