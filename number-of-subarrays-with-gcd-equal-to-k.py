class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        start = 0
        count =0
        while start < len(nums):
            cur_gcd = nums[start]
            end = start
            
            while end < len(nums):
                
                cur_gcd = self.gcd(cur_gcd, nums[end])
                if cur_gcd == k:
                    count+=1
                elif cur_gcd < k:
                    break
                    
                end+=1
            start+=1
        return count

    def gcd(self, a, b):
        
        if b == 0:
            return a
        return self.gcd(b, a%b)
        
