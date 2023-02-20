# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # dummy = ListNode(0)
        # dummy.next = head
        mid = head
        
        while head:
            head = head.next
            if head == None:
                return mid
            else:
                mid = mid.next
                head = head.next

        
        return mid
        