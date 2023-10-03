class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        costs.sort(key = lambda x: x[0]-x[1])
        ans = 0
        for i, cost in enumerate(costs):
            if i < len(costs)//2:
                ans+=cost[0]
            else:
                ans+=cost[1]
        return ans