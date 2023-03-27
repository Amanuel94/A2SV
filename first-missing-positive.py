class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        i = 0
        while i < len(nums):
            # print(nums, i)
            if 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] =  nums[i], nums[nums[i]-1]
            else:
                i+=1 
        # print(nums)     
        for i, c in enumerate(nums):
            if c - i != 1:
                return i+1
            
        return len(nums)+1
#                 
        
    
