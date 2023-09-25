class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        n = len(scores)
        indices = sorted(list(range(n)), key = lambda x: (ages[x], scores[x]))

        dp = [scores[indices[i]] for i in range(n)]
        
        for i in range(n):
            score = scores[indices[i]]
            for j in range(i):
                if scores[indices[j]] <= score:
                    dp[i] = max(dp[i], dp[j]+score)


        return max(dp)