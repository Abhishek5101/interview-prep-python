def added_str(num1, num2):
	ans = ""
	str_num1 = str(num1)
	str_num2 = str(num2)
	for i in range(len(str_num1)):
		ans += str(int(str_num1[i]) + int(str(str_num2[i])))
	return print(ans)


added_str(180, 190)
"""
95, 98
9 + 9 = 18
5 + 8 = 13

return 1813

180 190
2170
"""
