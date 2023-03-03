class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left_pointer = max(weights)
        right_pointer = sum(weights)
        res = 0
      
    
        while left_pointer <= right_pointer:
            mid = left_pointer + (right_pointer - left_pointer) // 2
            
            if self.helper(weights, days, mid):
                res = mid
                right_pointer = mid - 1
                
            else:
                left_pointer = mid + 1
                
                
        return res
    
    def helper(self, we, da, mid):
        res = 0
        count = 1
        
        for i in we:
            if res + i <= mid:
                res += i
                
            else:
                count += 1
                res = i
            
      
        return count <= da