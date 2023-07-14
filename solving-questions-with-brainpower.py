class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        """
        the maximum number of points that can be earned by solving the
        ith question is the maximum of pointi + the maximum score
        earned by solving all questions after brainpoweri
        """

        dp =  [0]*len(questions)
        dp[-1] = questions[-1][0]
        n = len(questions)
        for i in range(n-2,-1, -1):
            point, brainpower = questions[i]
            if i + brainpower+1 < n:
                dp[i]= max(dp[i+1], point+dp[i+brainpower+1])
            else:
                dp[i] =max(dp[i+1], point)
        return dp[0]