class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        """
        last dig low : 1 1 3 3 3
        last dig high: 1 2 2 4 4

        """

        n = len(nums)

        low = [0]*n
        high = [0]*n

        low[0] = high[0] =1

        for i in range(1, n):
            cur = nums[i]
            max_low = max_high = 0
            for j in range(0, i):
                if nums[j] < cur and low[j] > max_low:
                    max_low = low[j]
                elif nums[j] > cur and high[j] > max_high:
                    max_high = high[j]
            high[i] = max_low+1
            low[i] = max_high+1
            
        return max(high[-1], low[-1])