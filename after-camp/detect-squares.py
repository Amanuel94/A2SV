class DetectSquares:

    def __init__(self):

        self.counter = {}
        

    def add(self, point: List[int]) -> None:
        if tuple(point) in self.counter:
            self.counter[tuple(point)]+=1
        else:
            self.counter[tuple(point)] = 1
    

    def count(self, point: List[int]) -> int:

        ans = 0
        x, y = point
        for p in self.counter:
            px, py = p
            if abs(x - px) != abs(y - py) or x == px or y == py:
                continue
            ans+=self.counter.get(p, 0)*self.counter.get((px, y), 0)*self.counter.get((x, py),0)
        
        return ans
            

        
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)