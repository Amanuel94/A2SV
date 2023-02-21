# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        
        headOfEven =  head.next
        prevEven = headOfEven
        prevOdd = head
        
        while(prevOdd and prevEven and prevEven.next):
            
            nextOdd = prevOdd.next.next
            nextEven = prevEven.next.next
            
            prevOdd.next = nextOdd
            prevEven.next = nextEven
            
            prevOdd = nextOdd
            prevEven = nextEven
        prevOdd.next = headOfEven
        return head
        
        