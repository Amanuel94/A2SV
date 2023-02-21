# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        while(node.next != None):
            node.val = node.next.val
            if node.next.next != None:
                node = node.next
            else:
                node.next = None