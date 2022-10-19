# A program script to explore the heap sort algorithm.

# Walkthrough Video Link: https://www.youtube.com/watch?v=V1K7bYcAhXY

def tidy_heap(heap, index):
	LEFT = (2 * index) + 1
	RIGHT = (2 * index) + 2

	large = index
	if LEFT < len(heap) and heap[large] < heap[LEFT]:
		large = LEFT
	if RIGHT < len(heap) and heap[large] < heap[RIGHT]:
		large = RIGHT

	if large != index:
		heap[index], heap[large] = heap[large], heap[index]
		tidy_heap(heap, large)
	return heap

def heap_sort(array):
	sort_array = []
	heap = array.copy()
	while heap:
		# Create the max heap.
		for i in range((len(heap)//2)-1, -1, -1):
			tidy_heap(heap, i)

		# Storing the max value in the sort array.
		sort_array.insert(0, heap[0])
		heap[0], heap[-1] = heap[-1], heap[0]
		heap.pop(-1)
	return sort_array

array = [10, 3, 1, 9, 12, 48, 4, 9, 2, 6, 3]
print(f'Unsorted Array: {array}')

test = heap_sort(array)
print(f'Sorted Array: {test}')
