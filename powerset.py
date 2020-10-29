# Time and Space (2^n * n)

def powerset(array):
	subsets = [[]]
	for element in array:
		for i in range(len(subsets)):
			current_subset = subsets[i]
			print(current_subset + [element])
			subsets.append(current_subset + [element])
	return subsets

powerset([1, 2, 3])