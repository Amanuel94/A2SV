class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        
        high = max(nums)
        
        
        while low < high:
            
            mid =  low + (high-low)//2
    
            # print(self.div(nums, mid), low, mid, high)
        
            if self.div(nums, mid) <= threshold:
                
                high = mid
                
            else:
                low = mid + 1
                
        return high
    
    
    
    def div(self, nums, mid):
        ans = 0
        for num in nums:
            if num <= mid:
                ans += 1
            else:
                ans += math.ceil(num/mid)
        
        return ans
                