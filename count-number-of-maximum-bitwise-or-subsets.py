class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        count = 0
        
        def subsetOR(nums):
            ans = 0
            for num in nums:
                ans|=num
            return ans
        
        def validSubsetCount(nums, subset, i):
            nonlocal count
            if i == len(nums):
                if subsetOR(subset) == max_OR:
                    count+=1
                return 
            
            subset.append(nums[i])
            validSubsetCount(nums, subset, i+1)
            subset.pop()
            validSubsetCount(nums, subset, i+1)
                
                
        max_OR = subsetOR(nums)
        validSubsetCount(nums, [], 0)
        
        return count
