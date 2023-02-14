class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(b) > len(a):
            a, b  = b, a
        
        i = len(a)-1
        j = len(b)-1
        
    
        
        sum_ = ""
        carry = 0
        
        while i > -1 and j >-1:
            
            sum_ =  str((carry + int(a[i]) + int(b[j]))%2) + sum_
            carry = (int(a[i]) + int(b[j]) + carry)//2
            i-=1
            j-=1
            
        while i > -1:
            sum_ =  str(int((carry + int(a[i]))%2)) + sum_
            carry = (int(a[i]) + carry)//2
            i-=1
        sum_ = "1"+ sum_ if carry else sum_
        
        return sum_
        
        
        