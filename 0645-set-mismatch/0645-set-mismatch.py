class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        c = Counter(nums)
        lost = duplicated = 0
        for i in range(1, len(nums)+1):
            if c.get(i) == 2:
                duplicated = i
            elif c.get(i,0) == 0:
                lost = i
        return [duplicated, lost]