class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        pre = [0]
        
        for i in nums:
            pre.append(i + pre[-1])
        return pre[1:]