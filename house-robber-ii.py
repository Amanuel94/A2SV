class Solution:
    def rob(self, nums: List[int]) -> int:

        """
        1 2 3 4 5 6 7 
        """
        if len(nums)==1:
            return nums[0]
        memo = {}
        def dp(ptr, flag):
            if ptr == 0:
                memo[(ptr, flag)] = nums[0]*(1-flag)
            elif ptr == 1:
                memo[(ptr, flag)] = max(nums[0]*(1-flag), nums[1])
            else:
                if (ptr-1, flag) in memo:
                    prev1 = memo[(ptr-1, flag)]  
                else:
                    prev1 = dp(ptr-1, flag)
                
                if (ptr-2, flag) in memo:
                    prev2 = memo[(ptr-2, flag)]  
                else:
                    prev2 = dp(ptr-2, flag)
                memo[(ptr, flag)] = max(prev1, prev2+nums[ptr])

            return memo[(ptr, flag)]

        with_last_house = dp(len(nums)-1, 1)
        no_last_house = dp(len(nums)-2, 0)
        return max(with_last_house, no_last_house)