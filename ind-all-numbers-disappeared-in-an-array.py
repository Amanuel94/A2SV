class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        i = 0
        while i < len(nums):
            
            if nums[i] - i == 1:
                i+=1
                
            elif nums[nums[i] - 1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            elif nums[nums[i]-1] == nums[i]:
                i+=1
                
        ans = []    
        for i, n in enumerate(nums):
            if n != i+1:
                ans.append(i+1)
        return ans
        
       
