class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        # if n%4 > 0 and n != 1:
        #     return False
        # elif n == 1:
        #     return True
        # elif n == 0:
        #     return False
        # else:
        #     return self.isPowerOfFour(n//4)
        
        n = float(n)
        
        if n == 1.0:
            return True
        elif n < 1.0:
            return False
        else:
            return self.isPowerOfFour(n/4)
      
            
        
        
        