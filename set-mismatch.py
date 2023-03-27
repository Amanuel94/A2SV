class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        i = 0
        while i < len(nums):
            
            if nums[i] - i == 1:
                i+=1
            elif nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            elif nums[nums[i]-1] == nums[i]:
                i+=1
                
        for i, c  in enumerate(nums):
            if c - i -1:
                return [c, i+1]
        
        
