# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        vals = []
        dummy = head
        while head:
            vals.append(head.val)
            head = head.next
        # vals = vals[::-1
        head = dummy
        while head:
            head.val = vals.pop()
            head = head.next
        return dummy
        
        
        