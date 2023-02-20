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

        interset = ListNode()
        
        if not head:
            return False
 
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                break
                
                
        if not fast or not fast.next:
            return None
        else:
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return fast
        
            





