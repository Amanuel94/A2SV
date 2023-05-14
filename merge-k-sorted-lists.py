# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for list_ in lists:
            while list_:
                heappush(heap, list_.val)
                list_ = list_.next

        # print(heap)
        head = None
        if heap:
            head = ListNode(heappop(heap))
        dummy  = ListNode()
        dummy.next = head
        while heap:
            head.next = ListNode(heappop(heap))
            head = head.next
        return dummy.next