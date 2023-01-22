class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        iters = set()
        cur = n       
        while  cur not in iters and cur != 1:
            iters.add(cur)
            
            op = 0
            for digit in str(cur):
                op+= int(digit)**2
                
            cur = op            
            
        if cur == 1:
            return True
        else:
            return False
        