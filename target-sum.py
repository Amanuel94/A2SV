class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        """
        the required number = # exp that sum to target - num[-1] + 
        # exp with sum target+num[-1]
        """
        memo = defaultdict(int)
        def dp(ptr, target):
            if ptr == 0:
                memo[(ptr, target)] = int(nums[0] == target) + int(nums[0] == -target)
            else:
                minus_part, plus_part = 0, 0 
                if (ptr-1, target-nums[ptr]) in memo:
                    minus_part = memo[(ptr-1, target-nums[ptr])]
                else:
                    minus_part = dp(ptr-1, target-nums[ptr])
                
                if (ptr-1, target+nums[ptr]) in memo:
                    plus_part = memo[(ptr-1, target+nums[ptr])]
                else:
                    plus_part = dp(ptr-1, target+nums[ptr])
                memo[(ptr, target)] = minus_part+plus_part
            return memo[(ptr,target)]
        return dp(len(nums)-1, target)