class Solution:
    def uniquePaths(self, m: int, n: int, memo = defaultdict(int)) -> int:

        # if m == 1 or n == 1:
        #     memo[(m, n)] = 1
        # else:
        #     if (m, n) not in memo:     
        #         memo[(m,n)] = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        # return memo[(m, n)]

        # dp = [[0]*n for i in range(m)]
        # dp[0][0]=1
        # for i in range(m):
        #     for j in range(n):
        #         if j < n-1:
        #             dp[i][j+1] += dp[i][j]
        #         if i < m-1:
        #             dp[i+1][j] += dp[i][j]
        # return dp[m-1][n-1]

        return math.comb(n+m-2, n-1)