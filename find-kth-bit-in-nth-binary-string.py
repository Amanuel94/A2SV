class Solution(object):
    def findKthBit(self, n, k):
        return self.s(n)[k+1]
        
    
    def s(self, n):
        if n == 1:
            return "0b0"
        else:
            b = self.s(n-1)
            
            return "0b" + b[2:] + "1" + self.reverse(self.invert(len(b)-2, b))[2:]
        
    
    def invert(self, n, b):
        b = bin(int(b, 2) ^ (2**n)-1)
        return "0b" + (n - len(b[2:]))*"0" + b[2:]
        
    def reverse(self, b):
        b = b[2:][::-1]
        return "0b" + b
