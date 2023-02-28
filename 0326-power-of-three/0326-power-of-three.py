class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = float(n)
        
        if n == 1.0:
            return True
        if n < 1.0:
            return False
        else:
            return self.isPowerOfThree(n/3)