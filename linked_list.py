"""
Linked List: O(n) lookup and O(1) append
"""


class Node:
	def __init__(self, value=None):
		self.value = value
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = Node()
		
	def append(self, value):
		current = self.head
		new_node = Node(value)
		while current.next is not None:
			current = current.next
		current.next = new_node
		
	def length(self):
		count = 0
		current = self.head
		while current.next is not None:
			count += 1
			current = current.next
		return count

	def display(self):
		# elements = []
		# current = self.head
		# while current.next is not None:
		# 	current = current.next
		# 	elements.append(current.value)
		# return elements
		current = self.head
		while current.next is not None:
			current = current.next
			print(current, current.value)
		return
	
	def find(self, index):
		if index > self.length() or index < 0:
			return None
		curr_index = 0
		current = self.head
		while current:
			current = current.next
			if curr_index == index:
				return current.value
			curr_index += 1
	
	def erase(self, index):
		curr_index = 0
		current = self.head
		while current.next is not None:
			prev = current
			current = current.next
			if curr_index == index:
				prev.next = current.next
				return current.value
			curr_index += 1
		

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
print(ll.length())