class Solution(object):
    def removeNthFromEnd(self, head, n):
        i = 0
        ptr = head
        new_head = ListNode(0)
        new_ptr =  new_head
        while ptr != None:
            ptr = ptr.next
            i+=1
        j = 1
        if i != n:
            while head != None:
                if j!= i - n:
                    new_ptr.next = ListNode(head.val, head.next)
                    head = head.next
                else:
                    new_ptr.next = ListNode(head.val, head.next.next)
                    head = head.next.next
                new_ptr = new_ptr.next
                j+=1
            return new_head.next
        else:
            return head.next