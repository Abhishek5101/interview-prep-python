def mutate(arr):
	b = arr[:]
	for i in range(len(arr)):
		if i == 0:
			b[i] = 0 + arr[i] + arr[i+1]
		elif i == len(arr)-1:
			b[i] = arr[i-1] + arr[i] + 0
		else:
			b[i] = arr[i-1] + arr[i] + arr[i+1]
	return print(b)


mutate([1, 2, 3, 4])
# [3, 6, 9, 7]