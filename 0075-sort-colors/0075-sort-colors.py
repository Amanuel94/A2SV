class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        # use insertion sort
        i = 1
        number_of_balls = len(nums)
        
        while i < number_of_balls:
            j = i
            while j > 0 and nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j-=1
        
            i+=1
        
        return nums
        