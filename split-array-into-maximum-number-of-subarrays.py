class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:

        min_prod = list(accumulate(nums, lambda x, y: x & y))[-1]

        if min_prod > 0:
            return 1
            
        count = 0
        cur_prod = nums[0]

        left = 0
        for i in range(len(nums)):
            if cur_prod == min_prod:
                count+=1
                if i < len(nums)-1:
                    cur_prod = nums[i+1]
            if i < len(nums)-1:
                cur_prod&=nums[i+1]

        return count