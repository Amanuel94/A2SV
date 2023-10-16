class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True for i in range(n+1)]
        p = 2
        while p * p <= n:
            if prime[p]:
                j = p*p
                while j < n+1:
                    prime[j] = False
                    j+=p
            p += 1
        ans = 0
        for i in range(2, n):
            if prime[i]:
                ans +=1
        return ans