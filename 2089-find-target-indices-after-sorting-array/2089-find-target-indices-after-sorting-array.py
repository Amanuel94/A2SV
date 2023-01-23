class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        less = 0
        same = 0
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                same+=1
            elif nums[i] < target:
                less+=1
        for i in range(same):
            res.append(less + i)
        return res
            
                
        