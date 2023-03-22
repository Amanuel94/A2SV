# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        
        stack = []
        answer = []
        
        #reverse list
        
        r_head = None
        
        while head:
            temp = ListNode(head.val)
            temp.next = r_head
            r_head = temp
            head = head.next
        
        #traverse and stack
        
        while r_head:
        
            while stack and stack[-1] <= r_head.val:
                x = stack.pop()
                
            if stack:
                answer.append(stack[-1])
            else:
                answer.append(0)
                
            stack.append(r_head.val)
            
            r_head = r_head.next
            
        
        #report
        return answer[::-1]
 
        
    '''
    
    2  1  5
    5  1  2
    
    0  5  2
    5
    
    2 7 4 3 5
    5 3 4 7 2
    
    5 3 4 7 2 
    0 5 5 0 7
    7
    '''
