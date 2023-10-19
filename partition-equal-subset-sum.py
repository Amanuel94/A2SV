class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        target_sum  = sum(nums)
        if target_sum % 2:
            return False
        target_sum//=2

        @cache
        def dp(target_sum, i):
            if target_sum == 0:
                return True
            if target_sum < 0 or i == len(nums):
                return False
            return dp(target_sum-nums[i], i+1) or dp(target_sum, i+1)
        
        return dp(target_sum, 0)