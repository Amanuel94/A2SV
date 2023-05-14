class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = sorted(nums)[-k:]
        heapify(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) == self.k:
            x = heappop(self.heap)
            heappush(self.heap, max(x, val))
            return self.heap[0]
        else:
            heappush(self.heap, val)
            return self.heap[0]

     
        


   

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)