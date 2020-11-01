# This is an input class. Do not edit.
class LinkedList:
	def __init__(self, value):
		self.value = value
		self.next = None


def removeKthNodeFromEnd(head, k):
	count = 1
	first = head
	second = head
	while count <= k:
		second = second.next
		count += 1
	if second is None:
		first.value = first.next.value
		first.next = first.next.next
		return
	while second.next is not None:
		first = first.next
		second = second.next
	first.next = first.next.next
