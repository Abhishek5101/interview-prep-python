def bubbleSort(array):
	for _ in range(len(array)):
		for i in range(len(array)-1):
			if array[i] > array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]
	return array
