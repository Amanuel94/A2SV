class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        #dp[i][j] = [m, b], m is the minimum in the path, b is best current sum in path 
        if len(dungeon) == 1 and len(dungeon[0]) == 1:
            return max(1 - dungeon[0][0],1)

        n = len(dungeon)
        m = len(dungeon[-1])
        dp = [[float('inf') for i in range(m)] for j in range(n)]

        dp[n-1][m-1] = max(1-dungeon[-1][-1], 1)

        # for i in range(n-1, 0, -1):
        #     dp[i-1][-1] = max(1, dp[i][-1]-dungeon[i-1][-1])
        
        # for i in range(m-1, 0, -1):
        #     dp[-1][i-1] = max(1, dp[-1][i]-dungeon[-1][i-1])

       
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i > 0:
                    dp[i-1][j] = min(max(1, dp[i][j]-dungeon[i-1][j]), dp[i-1][j])
                if j > 0:
                    dp[i][j-1] = min(max(1, dp[i][j]-dungeon[i][j-1]), dp[i][j-1])
        print(dp)
        
        return dp[0][0]

        

        # 1 -1 1 -1 1
        # -1 1 -1 1 -1
        # -1 1 -1 1 -1
        # 1 -1 1 -1 1
        # -1 1 -1 1 -1