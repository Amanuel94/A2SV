# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        vals = []
        dummy = ListNode(0)
        dummy.next= head
        while head:
            vals.append(head.val)
            head = head.next
        vals =  vals[:left-1]+ vals[left-1:right][::-1] + vals[right:]
        print(vals)
        head = dummy.next
        i = 0
        while head:
            head.val = vals[i]
            head = head.next 
            i+=1
        return dummy.next
        