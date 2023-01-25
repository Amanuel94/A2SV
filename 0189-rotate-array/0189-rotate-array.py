class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        arr = []
        [arr.append(i) for i in nums]
        
        i = 0
        while i < len(nums):
            nums[i] = arr[(i-k)%len(nums)]
            i+=1
        