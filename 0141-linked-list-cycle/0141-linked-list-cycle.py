# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
#         nodes = set()
#         while head:
#             if head in nodes:
#                 return True
#             else:
#                 nodes.add(head)
#             head= head.next
#         return False
        if not head:
            return False

        slow = head
        fast = head.next
        
        while fast and fast.next:
            if fast == slow:
                return True
            else:
                fast = fast.next.next
                slow = slow.next
        return False
        
            





