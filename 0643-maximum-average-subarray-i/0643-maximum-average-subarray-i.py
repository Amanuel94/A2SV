class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum_ = sum(nums[:k])
        max_ = sum_
        
        i = 0
        while i < len(nums)-k:
            sum_ = sum_ - nums[i] + nums[i+k]
            max_ = max(max_, sum_)
            i+=1
        return float(max_)/k
            
        