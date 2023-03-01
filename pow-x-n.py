class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1    
        if n < 0:
            return (1/self.myPow(x, -n))
        return self.myPow(x*x, n/2)*(x**(n%2))
