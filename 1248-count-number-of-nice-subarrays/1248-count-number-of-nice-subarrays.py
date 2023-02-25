class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        return self.leqK(nums, k) - self.leqK(nums, k-1)
        
        
    def leqK (self, nums, k):
        left = 0
        ans = 0
        odds =  0

        for right in range(len(nums)):
            odds+=nums[right]%2
            while odds - k > 0:
                odds-=nums[left]%2
                left+=1
            ans+= right-left+1
        return ans
        