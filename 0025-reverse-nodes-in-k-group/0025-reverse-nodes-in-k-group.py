# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k, remaining = None):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        #if remaining number of node is not known calculate it
        if remaining == None:
            remaining = 0 
            dummy = ListNode(0)
            dummy.next = head
            while head:
                head = head.next
                remaining+=1
            head = dummy.next
        
        #if remaining <  k return head
        if remaining  < k:
            return head
        
        elif remaining == k:
            prev = None
            curr = head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        else:
            #dummy points to the original head
            dummy = ListNode(0)
            dummy.next = head

            #reverse the first k nodes
            prev = head
            cur = prev.next
            nxt = cur.next
            prev.next = None

            for i in range(k-1):
                # print(cur.val)
                cur.next = prev
                prev = cur
                cur =  nxt
                nxt = nxt.next
            #join the original head to the head after recursion
            dummy.next.next = self.reverseKGroup(cur, k, remaining - k)

            return prev
        
        
        
        
        
        
        
        