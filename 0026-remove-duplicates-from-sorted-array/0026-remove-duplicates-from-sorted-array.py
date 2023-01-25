class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = 0
        r = 1
        while r < len(nums):
            if nums[l] == nums[r]:
                if l!= r:
                    nums[r] = 101
                r+=1
            elif l < r:
                l+=1
        nums.sort()
        nums.append(101)
        return nums.index(101)
                
        
        