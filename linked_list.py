"""
Linked List: O(n) lookup and O(1) append
"""


class Node:
	def __init__(self, value):
		self.value = value
		self.next = None