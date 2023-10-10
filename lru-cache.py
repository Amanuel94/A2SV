class ListNode:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.prev =  None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):

        self.dict = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity
        

    def get(self, key: int) -> int:

        if key in self.dict:
            node = self.dict[key]
            prev, nxt = node.prev, node.next
            prev.next = nxt
            nxt.prev = prev
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev.next = node
            self.tail.prev = node
            return node.val
        return -1
            
        

    def put(self, key: int, value: int) -> None:

        if key in self.dict:
            node = self.dict[key]
            prev, nxt = node.prev, node.next
            prev.next = nxt
            nxt.prev = prev
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev.next = node
            self.tail.prev = node
            node.val = value
            return

        if self.cap == 0:
    
            k = self.head.next.key
            self.head.next.next.prev = self.head
            self.head.next = self.head.next.next
            del self.dict[k]
            self.cap+=1


        newNode = ListNode(key, value)
        newNode.prev = self.tail.prev
        newNode.next =  self.tail
        self.tail.prev.next = newNode
        self.tail.prev = newNode
        self.cap-=1

        self.dict[key] = newNode
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)