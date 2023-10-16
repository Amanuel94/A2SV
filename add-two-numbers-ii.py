# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        r1 = ListNode()
        r2 = ListNode()
        h1, h2 = ListNode(0, r1), ListNode(0, r2)
        while l1:
            newNode = ListNode(l1.val)
            newNode.next = r1.next
            r1.next = newNode
            l1 = l1.next
        
        while l2:
            newNode = ListNode(l2.val)
            newNode.next = r2.next
            r2.next = newNode
            l2 = l2.next

        ans = ListNode()
        carry = 0
        while r1.next and r2.next:
            newNode = ListNode((carry + r2.next.val + r1.next.val)%10)
            carry = (carry + r2.next.val + r1.next.val)//10
            newNode.next = ans.next
            ans.next = newNode
            r1.next = r1.next.next
            r2.next = r2.next.next


        while r1.next:
            newNode = ListNode((carry + r1.next.val)%10)
            carry = (carry + r1.next.val)//10
            newNode.next = ans.next
            ans.next = newNode
            r1.next = r1.next.next
        
        while r2.next:
            newNode = ListNode((carry + r2.next.val)%10)
            carry = (carry + r2.next.val)//10
            newNode.next = ans.next
            ans.next = newNode
            r2.next = r2.next.next
        if carry:
            newNode = ListNode(carry)
            newNode.next = ans.next
            ans.next = newNode
            
        return ans.next