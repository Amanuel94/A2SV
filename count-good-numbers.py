class Solution:
    def countGoodNumbers(self, n: int) -> int:

        MOD = 10**9+7

        @cache
        def recur(n, s):
            if n == 1:
                return 5-s
            if n == 0:
                return 0
    
            
            if n%2 == 0:
                if (n//2) %2 == 0:
                    return pow(recur(n//2, s), 2, MOD)
                else:
                    return (recur(n//2, 1-s)%MOD)*(recur(n//2, s)%MOD)
            else:
                return (5-s)*recur(n-1, s)%MOD
        return recur(n, 0)%MOD