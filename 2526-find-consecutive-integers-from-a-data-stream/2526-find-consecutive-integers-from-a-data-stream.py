class DataStream(object):

    def __init__(self, value, k):
        """
        :type value: int
        :type k: int
        """
        self.li = []
        self.val = value
        self.strike = 0
        self.k = k
        
        
        

    def consec(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == self.val:
            self.strike+=1
        else:
            self.strike = 0
        self.li.append(num)
        if self.strike >=self.k:
            return True
        else:
            return False
        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)