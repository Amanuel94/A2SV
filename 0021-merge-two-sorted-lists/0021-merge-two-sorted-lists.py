# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode(0)
        ptr = head
        ptr1 = list1
        ptr2 = list2
        while ptr1 != None and ptr2 != None:
            if ptr1.val <= ptr2.val:
                ptr.next = ListNode(ptr1.val)
                ptr1 = ptr1.next
            else:
                ptr.next = ListNode(ptr2.val)
                ptr2 = ptr2.next
            ptr = ptr.next
        while ptr1 != None:
            ptr.next = ListNode(ptr1.val)
            ptr1 = ptr1.next
            ptr = ptr.next
        while ptr2 != None:
            ptr.next = ListNode(ptr2.val)
            ptr2 = ptr2.next
            ptr = ptr.next
        return head.next
            
        