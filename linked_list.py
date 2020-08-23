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
			current = current.next
			count += 1
		return count

	def prepend(self, value):
		new_node = Node(value)
		previous_first = self.head.next
		self.head.next = new_node
		new_node.next = previous_first
