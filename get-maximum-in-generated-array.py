class Solution:
    def getMaximumGenerated(self, n: int) -> int:

        memo = {}
        ans = -float('inf')
        def getN(n):
            nonlocal ans
            if n == 0 or n == 1:
                memo[n] = n
            elif n == 2:
                memo[n] = 1
            elif n in memo:
                return memo[n]
            else:
                if n//2 in memo:
                    summand1 = memo[n//2]
                else:
                    summand1 = getN(n//2)
                if (n//2 +1) in memo:
                    summand2 = memo[n//2 +1]
                else:
                    summand2 = getN(n//2 +1)
                memo[n] = summand1 + (n%2)*summand2
            return memo[n]
        for  i in range(0, n+1):
            ans = max(ans, getN(i))
        return ans