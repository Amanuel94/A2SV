class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos = []
        neg = []
        
        for num in nums:

            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        res = []
        for index in range(len(nums)/2):
            res.append(pos[index])
            res.append(neg[index])

        return res
