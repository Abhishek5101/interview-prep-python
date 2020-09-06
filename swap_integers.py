# def swap_integers(number):
# 	ans = ''
# 	str_num = str(number)
# 	popped = ''
# 	if len(str_num) % 2 != 0:
# 		popped = str_num[-1]
# 		str_num = str_num[:len(str_num)-1]
# 	for i in range(0, len(str_num), 2):
# 		ans += str_num[i+1]
# 		ans += str_num[i]
# 	if popped:
# 		ans += popped
# 	return ans
#
#
# print(swap_integers(1234567))


def swap_ints(number):
	ans = ""
	odd = False
	str_num = str(number)
	if len(str_num) % 2 != 0:
		last = int(str_num[-1])
		odd = True
		number = number - last
		number = number // 10
	for i in range(0, len(str_num)-1, 2):
		ans += str_num[i+1]
		ans += str_num[i]
	if odd:
		ans += str(last)
	return print(ans)


swap_ints(123456789)