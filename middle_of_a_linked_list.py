# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = 1
        current = head
        while current:
            current = current.next
            length += 1
        if length%2 == 0:
            middle =  length//2
        else:
            middle = length//2 + 1
        if middle == 1:
            return head
        tracker = 1
        current = head
        while current:
            tracker += 1
            current = current.next
            if tracker == middle:
                return current