class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        """
        the minimum largest digit occurs when the numbers are equal. Thus try to equally
        distribute the numbers
        """

        pre = 0
        ans = float('-inf')
        for n, num in enumerate(nums):
            pre+=num
            ans = max(ans, ceil(pre/(n+1)))
        return ans