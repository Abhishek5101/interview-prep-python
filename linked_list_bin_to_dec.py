class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bin = '0b'
        current = head
        while current:
            bin += str(current.val)
            current = current.next
        return int(bin, 2)