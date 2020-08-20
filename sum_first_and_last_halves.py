def first_and_last_halves(num):
	first_half = str(num)[:len(str(num))//2]
	last_half = str(num)[len(str(num))//2:]
	
	first_half_sum = 0
	last_half_sum = 0
	
	for digit in first_half:
		first_half_sum += int(digit)
	
	for digit in last_half:
		last_half_sum += int(digit)
	
	return first_half_sum == last_half_sum



def first_and_last_halves_with_array(number):
	left = 0
	right = len(str(number))-1
	first_half_sum = 0
	last_half_sum = 0
	while left < right:
		first_half_sum += int(str(number)[left])
		last_half_sum += int(str(number)[right])
		left += 1
		right -= 1
	print(first_half_sum, last_half_sum)
	return first_half_sum == last_half_sum

print(first_and_last_halves_with_array(239017))