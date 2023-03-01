class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        
        pre = [0]*1001
        
        for trip in trips:
            num, from_, to_ = trip
            pre[from_]+=num
            pre[to_]-=num
        
        if pre[0] > capacity: return False
        
        i = 1
        while i < len(pre):
            pre[i]+=pre[i-1]
            if pre[i] > capacity:
                return False
            i+=1
        return True
