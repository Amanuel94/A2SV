class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:



        memo = defaultdict(float)
        def dp(i, j, k):
            if not (0 <= i < n) or not(0<=j<n):
                return 0
                
            if k == 0:
                 return 1
            if (i, j, k) in memo:
                return memo[(i,j,k)]
            

            
            memo[(i,j,k)] += dp(i+1, j+2, k-1)
            memo[(i,j,k)] += dp(i+1, j-2, k-1)
            memo[(i,j,k)] += dp(i+2, j+1, k-1)
            memo[(i,j,k)] += dp(i+2, j-1, k-1)
            memo[(i,j,k)] += dp(i-1, j+2, k-1)
            memo[(i,j,k)] += dp(i-1, j-2, k-1)
            memo[(i,j,k)] += dp(i-2, j+1, k-1)
            memo[(i,j,k)] += dp(i-2, j-1, k-1)

            memo[(i,j,k)]/=8
            return memo[(i, j, k)]

        return dp(row, column, k)