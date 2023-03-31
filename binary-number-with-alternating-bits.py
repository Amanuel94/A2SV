class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        return self.hasAlt(n)
    
    
    def hasAlt(self, n = 0, prev = 2):
        
        if n == 0 or n == 1:
            
            return True
        
        elif n == 3:
            return False
        
        if prev != n & 1:
            return self.hasAlt(n>>1, n&1)
        else:
            return False
        
