def balancedBrackets(string):
    opening = ['(', '{', '[']
	closing = [')', '}', ']']
	close_to_open = {")":"(", "]":"[", "}":"{"}
	stack = []
	for char in string:
		if char in opening:
			stack.append(char)
		elif char in closing:
			if len(stack) == 0:
				return False
			elif close_to_open[char] == stack[-1]:
				stack.pop()
			else:
				return False
	return len(stack) == 0