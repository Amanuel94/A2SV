class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        n = len(nums)
        less = [num for num in nums if num < pivot]
        greater = [num for num in nums if num > pivot]

        l = len(less)
        g = len(greater)
        ans = []
        for num in less:
            ans.append(num)

        ans.extend([pivot]*(n - l - g))

        for num in greater:
            ans.append(num)

        return ans
