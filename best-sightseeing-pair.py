class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        n =  len(values)

        dp = [float('-inf')]*n
        dp[-1] = values[-1]
        rtl_maximum = values[-1]-1
        i = n-2
        while i >= 0:
          dp[i] = max(dp[i+1],rtl_maximum+values[i])
          rtl_maximum = max(values[i], rtl_maximum)-1
          i-=1
        return dp[0]