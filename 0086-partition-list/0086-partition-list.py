# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        h = less = ListNode(0)
        gre = ListNode(0)
        app = gre
        
        while head:
            if head.val < x:
                less.next = head
                less = head
            else:
                gre.next = head
                gre = head
            head = head.next
        less.next = app.next
        gre.next = None
        return h.next
                
                
        
        
        