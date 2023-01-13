class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0

        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1] = 0

            i+=1
        
        p = len(nums)-1
        while i > 0:
            if nums[i] == 0:
                j = i
                while j < p:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    j+=1
                p-=1
            i-=1

        if nums[0] == 0:
            nums = nums[1:] + [0]
        return nums
