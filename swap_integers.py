def swap_integers(number):
	ans = ''
	str_num = str(number)
	popped = ''
	if len(str_num) % 2 != 0:
		popped = str_num[-1]
		str_num = str_num[:len(str_num)-1]
	for i in range(0, len(str_num), 2):
		ans += str_num[i+1]
		ans += str_num[i]
	if popped:
		ans += popped
	return ans


print(swap_integers(1234567))