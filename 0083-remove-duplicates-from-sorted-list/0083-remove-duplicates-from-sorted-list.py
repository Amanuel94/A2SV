class Solution(object):
    def deleteDuplicates(self, head):
        new_hd =  ListNode(0, head)
        ptr1 = new_hd
        prev = 301
        while head != None:
            if head.val == prev:
                head = head.next
            else:
                ptr1.next = ListNode(head.val)
                ptr1 = ptr1.next
                prev = head.val
                head = head.next  
        return new_hd.next