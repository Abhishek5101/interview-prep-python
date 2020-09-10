def twoNumberSum(array, targetSum):
	"""
	Sort the array, initialize left and right pointers
	get their sum and compare it to target
	if sum fall short, move the lp
	if sum is larger, move the rp
	"""
	array = sorted(array)
	left , right = 0, len(array)-1
	for i in range(len(array)):
		if array[left] + array[right] == targetSum:
			return [array[left], array[right]]
		elif array[left] + array[right] < targetSum:
			left += 1
		elif array[left] + array[right] > targetSum:
			right -= 1
	return []
