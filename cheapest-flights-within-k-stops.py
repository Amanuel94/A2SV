class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:



        dp = [inf]*n
        prev = [inf]*n
        dp[src] = 0
        prev[src]= 0

        for _ in range(k+1):
            for u, v, w in flights:
                dp[v] = min(dp[v], w + prev[u])
            prev = dp.copy()

        return dp[dst] if dp[dst] < inf else -1