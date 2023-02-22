# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        dummy =  ListNode(0)
        dummy.next = head
        rev = None
        while head:
            temp = ListNode(head.val)
            temp.next = rev
            rev = temp
            head = head.next
        head = dummy.next
        max_ = 0
        while head:
            max_ = max(head.val+rev.val, max_)
            head = head.next
            rev = rev.next
        return max_