# Feel free to add new properties and methods to the class.
class MinMaxStack:
	def __init__(self):
		self.min_max_stack = []
		self.stack = []
		
    def peek(self):
        return self.stack[len(self.stack)-1]

    def pop(self):
		self.min_max_stack.pop()
        return self.stack.pop()

    def push(self, number):
        new_min_max = {"minimum": number, "maximum": number}
		if len(self.min_max_stack) > 0:
			last_min_max = self.min_max_stack[len(self.min_max_stack) -1]
			new_min_max["minimum"] = min(last_min_max["minimum"], number)
			new_min_max["maximum"] = max(last_min_max["maximum"], number)
		self.min_max_stack.append(new_min_max)
		self.stack.append(number)

    def getMin(self):
        return self.min_max_stack[len(self.min_max_stack) -1]["minimum"]

    def getMax(self):
        # Write your code here.
        return self.min_max_stack[len(self.min_max_stack) -1]["maximum"]
