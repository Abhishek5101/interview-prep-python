def bubble_sort(array):
	for _ in range(len(array)):
		for i in range(len(array)-1):
			if array[i] > array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]
	return array


print(bubble_sort([2, 2, 1, 0, 2, 1, 0]))