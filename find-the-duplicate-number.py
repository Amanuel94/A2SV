class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        i = 0
        while i < len(nums):
            
            if nums[i] - i == 1:
                i+=1
                
            elif nums[nums[i] - 1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            elif nums[nums[i]-1] == nums[i]:
                i+=1
                
           
        for i, n in enumerate(nums):
            if n != i+1:
                return n
