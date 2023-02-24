class MyStack(object):

    def __init__(self):
        self.deque = deque()
        self.len = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.deque.append(x)
        self.len+=1
        

    def pop(self):
        """
        :rtype: int
        """
        self.len-=1
        return self.deque.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.deque[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.len ==  0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()