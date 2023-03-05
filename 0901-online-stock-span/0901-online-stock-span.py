class StockSpanner(object):

    def __init__(self):
        
        self.stack =[]
        self.pop_stack = []
        

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        
        pop_count = 0
        
        while self.stack and self.stack[-1] <= price:
            self.stack.pop()
            pop_count+=(1+self.pop_stack.pop())
            
            
        self.stack.append(price)
        self.pop_stack.append(pop_count)
        
        return pop_count+1
            
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)