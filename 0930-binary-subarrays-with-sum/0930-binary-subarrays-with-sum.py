class Solution(object):
    def numSubarraysWithSum(self, nums, k):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        def lessK(k):
            left = ans = 0
            sum_ = 0

            for right in range(len(nums)):

                sum_+=nums[right]

                while left <= right and sum_ > k:
                    sum_-=nums[left]
                    left+=1
                ans+= right-left+1
            return ans
        
        return lessK(k) - lessK(k-1)
        