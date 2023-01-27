class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.len = 0
        

    def get(self, index: int) -> int:
        if self.head and 0 <= index < self.len:
            dummy = Node(0)
            dummy.next = self.head
            # print(self.head.next.val)
            for i in range(index):
                self.head = self.head.next
            ans = self.head.val
            self.head = dummy.next
            return ans
        else:
            return -1
        

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.len+=1
            
    def addAtTail(self, val: int) -> None:
        if self.head:
            dummy =  Node(0)
            dummy.next = self.head
            while self.head.next:
                self.head = self.head.next
            new_node = Node(val)
            self.len+=1

            self.head.next = new_node
            self.head = dummy.next
        else:
            self.addAtHead(val)
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        if self.len >= index > 0:
            dummy =  Node(0)
            dummy.next = self.head
            i = 0
            while i < index-1:
                self.head = self.head.next
                i+=1
            new_node = Node(val)
            new_node.next = self.head.next
            self.head.next = new_node
            self.head = dummy.next
            self.len+=1
        elif index == 0:
            self.addAtHead(val)
        

    def deleteAtIndex(self, index: int) -> None:
        if 0 < index < self.len:
            dummy = Node(0)
            dummy.next = self.head
            i = 0
            while i < index - 1:
                self.head = self.head.next
                i+=1
            if index < self.len:
                self.head.next = self.head.next.next
          
            
            self.len-=1
            self.head = dummy.next
        elif index == 0:
            self.head = self.head.next
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)