class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        @cache
        def dp(i):
            if i == len(days):
                return 0
            
            return min(
                costs[0] + dp(i+1),
                costs[1] + dp(bisect_left(days, days[i]+7,)),
                costs[2] + dp(bisect_left(days, days[i]+30))
            )
        return dp(0)