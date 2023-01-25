class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        
        left = 0
        right = int(math.sqrt(c))
        
        while left <= right:
            cur = left**2 + right**2 
            if cur == c:
                return True
            elif cur < c:
                left+=1
            else:
                right-=1
        return False
                
        