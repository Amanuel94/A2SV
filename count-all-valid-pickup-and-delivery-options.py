class Solution:
    def countOrders(self, n: int) -> int:

        # f(n) = g(n)*f(n-1)

        # f(n) = p1 p2 p3 .. pn d1 d2 d3 .. dn = (2n - 1) + (2n, 2)

        N = pow(10, 9) + 7

        # @cache
        # def dp(n):
        #     if  n == 1:
        #         return 1
        #     return dp(n-1)*math.comb(2*n, 2)%N
        
        # return dp(n)
        return (math.perm(2*n)//pow(2, n))%N