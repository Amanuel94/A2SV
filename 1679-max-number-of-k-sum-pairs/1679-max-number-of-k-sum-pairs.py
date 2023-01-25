class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        
        l = 0
        r = len(nums)-1
        
        noOP = 0
        
        while l < r:
            
            if nums[l] + nums[r] == k:
                noOP+=1
                l+=1
                r-=1
            elif nums[l] + nums[r] < k:
                l+=1
            else:
                r-=1
        return noOP
        
        