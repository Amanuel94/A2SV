class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        left = [1]
        right = [1]
        
        for i in range(len(nums)):
            left.append(left[-1]*nums[i])
            right.append(right[-1]*nums[-i-1])
        right = right[::-1][1:]
        for i in range(len(nums)):
            left[i] = left[i]*right[i]
        return left[:-1]
        
        
        
        