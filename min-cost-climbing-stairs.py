class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cost.append(0)
        dp = [float('inf') for i in range(len(cost))] 

        dp[0] = cost[0]
        dp[1] = cost[1]

        i = 2
        while i < len(dp):
            dp[i] = min(dp[i-1], dp[i-2])+cost[i]
            i+=1
        return dp[-1]