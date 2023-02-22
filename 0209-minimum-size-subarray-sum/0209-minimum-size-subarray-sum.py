class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        right = 0
        left = 0

        sum_ = 0
        ans =  len(nums)
        if sum(nums) < s:
            return 0
        else:
            for right in range(len(nums)):
                sum_+= nums[right]

                while sum_ >= s:
                    ans = min(ans, right - left +1 )
                    sum_-=nums[left]
                    left+=1
            return ans




        