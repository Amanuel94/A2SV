class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        
        
        l = max(sum(piles)//h, 1)
        
        r = max(piles)
        
        store = 1
        
        while l <= r:
            mid = l+ (r-l)//2
            
            if self.rihannashelper(piles, mid, h):
                store = mid
                r = mid-1
            else:
                l = mid+1
                
        return store
                
                
                
    def rihannashelper(self, piles, mid, h):
        
        sum_ = 0
        
        for pile in piles:
            sum_+=(pile//mid)
            
            if pile%mid != 0:
                sum_+=1 
                
                
                
        return sum_ <= h
                
                
                
            
        