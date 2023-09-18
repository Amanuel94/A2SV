class Solution:
    def minSteps(self, n: int) -> int:
        
        # dp[i][0] not copied i As
        # dp[i][1] copied i As

        # dp[i][0] = min_over j dp[j][1] + 1
        # dp[i][1] = dp[i][1]+1

        dp = [[float('inf'), float('inf')] for i in range(n+1)]
        dp[1][0] = 0
        dp[1][1] = 1
        for i in range(1, n+1):
            for j in range(1, i):
                if i%j == 0:
                    dp[i][0] = min(dp[j][1]+(i//j-1), dp[i][0])
            dp[i][1] = dp[i][0]+1
        print(dp)
        return dp[n][0]