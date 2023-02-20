# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        nodes = set()
        while head:
            if head in nodes:
                return head
            else:
                nodes.add(head)
            head = head.next
        return None