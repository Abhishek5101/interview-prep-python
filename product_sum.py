# space com: At the peak, max no of recursion calls you have
# in the call stack

def productSum(array, multiplier=1):
	total_sum = 0
	for element in array:
		if type(element) is int:
			total_sum += element
		else:
			total_sum += productSum(element, multiplier +1)
	return total_sum * multiplier