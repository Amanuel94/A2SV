class Solution:
    def minSteps(self, n: int) -> int:
        
        ans = 0
        d = 2
        
        while d*d <= n:
            divides_n  = False
            while n%d == 0:
                n//=d
                ans+=d
                            
            d+=1
        return ans + n if n - 1 else ans
