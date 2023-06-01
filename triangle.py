class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        n = len(triangle)
        dp = defaultdict(lambda:float('inf'))
        dp[(0,0)] = triangle[0][0]
        ans = float('inf')
        for i in range(1, n):
            for j in range(-i, i+1, 2):
                dp[(i, j)] = min(dp[(i-1, j-1)], dp[(i-1, j+1)])+triangle[i][(j+i)//2]
                
        return min([dp[i] for i in dp if i[0] == n-1])