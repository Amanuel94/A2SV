class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """

        dic = {num:i for i, num in enumerate(nums)}

        for op in operations:
            nums[dic[op[0]]] = op[1]
            dic[op[1]] = dic.pop(op[0])
           
        return nums
