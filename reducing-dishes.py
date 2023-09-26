class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        satisfaction.sort()

        @cache
        def dp(pos, time):
            if pos == len(satisfaction)-1:
                return max(0, satisfaction[-1]*time)
            
            ans = 0
            ans = max(dp(pos+1, time+1)+satisfaction[pos]*time,
                      dp(pos+1, time), 
                      ans)
            return ans

        return dp(0, 1)