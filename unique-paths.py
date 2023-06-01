class Solution:
    def uniquePaths(self, m: int, n: int, memo = defaultdict(int)) -> int:

        # if m == 1 or n == 1:
        #     memo[(m, n)] = 1
        # else:
        #     if (m, n) not in memo:     
        #         memo[(m,n)] = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        # return memo[(m, n)]

        dp = [[1]*n for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1]+ dp[i-1][j]
        return dp[m-1][n-1]