class RandomizedSet:

    def __init__(self):
        self.list = []
        self.ind = {}
        
    
    def insert(self, val: int) -> bool:
        if val in self.ind:
            return False
        self.ind[val] = len(self.list)
        self.list.append(val) 
        return True
        
        

    def remove(self, val: int) -> bool:
        if val not in self.ind:
            return False

        ind = self.ind[val]
        self.ind[self.list[-1]] = self.ind[val]
        self.list[ind], self.list[-1] = self.list[-1], self.list[ind]
        del self.ind[val]
        self.list.pop()
        return True
        
        
        

    def getRandom(self) -> int:
        return random.choice(self.list)
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()