# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 and not list2:
            return None
        if list1 and list2:
            if list1.val < list2.val:
                head = ListNode(list1.val)
                head.next = self.mergeTwoLists(list1.next, list2)

            elif list2.val <= list1.val:
                head = ListNode(list2.val)
                head.next = self.mergeTwoLists(list1, list2.next)
        elif list1:
            head = ListNode(list1.val)
            head.next = self.mergeTwoLists(list1.next, list2)
            
        elif list2:
            head = ListNode(list2.val)
            head.next = self.mergeTwoLists(list1, list2.next)
            
        return head
    
            
            
            
            
        
        
