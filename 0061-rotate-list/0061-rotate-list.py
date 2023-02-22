# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if head == None or k == 0:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        reverse = None
        
        n = 0
        
        
        while head:
            temp = ListNode(head.val)
            temp.next = reverse
            reverse = temp
            head = head.next
            n+=1
        if n == 1 or k%n==0:
            return dummy.next
        
        head = dummy.next        
        new_head = None
        for _ in range(k%n):
            temp = ListNode(reverse.val)
            temp.next = new_head
            new_head = temp
            reverse = reverse.next
        for _ in range(n - k%n-1):
            head = head.next
        head.next = None
        n_dummy = ListNode(0)
        
        n_dummy.next = new_head
        while new_head.next:
            new_head = new_head.next
        new_head.next = dummy.next
        return n_dummy.next
            
        
        return new_head
                  
            
            
            
        