class Solution:
    def knightDialer(self, n: int) -> int:
        
        MOD = 10**9 + 7 
        H = [-1,-1,1,1,-2,-2,2,2]
        V = [-2,2,-2,2,1,-1,1,-1]

        def inBound(i, j):
            return 0 <= j < 3 and 0 <= i < 4

        memo = {} 
               
        def dp(i, j, n):
            nonlocal MOD
            if n == 1:
                return 1
            if(i, j, n) in memo:
                return memo[(i, j, n)]

            res = 0
            for k in range(8):
                tx, ty = i+H[k],j+V[k]
                if inBound(tx, ty) and ((tx, ty) not in [(3,0), (3,2)]):
                    res+=dp(tx, ty, n-1)%MOD

            memo[(i, j, n)] = res
            return res

        ans = 0
        for i in range(4):
            for j in range(3):
                if (i, j) not in [(3,0), (3,2)]:
                    ans+=dp(i, j, n)%MOD
        return ans%MOD