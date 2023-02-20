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
#         mid = head
#         head = head.next
        
#         while head:
#             head = head.next
#             mid = mid.next
#             if head:
#                 return mid
#             else:
#                 head = head.next

        ans = []
        while head:
            ans.append(head)
            head = head.next
        return ans[len(ans)//2]
            
        