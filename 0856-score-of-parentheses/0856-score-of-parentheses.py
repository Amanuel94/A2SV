class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0.0]
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append(0)
                i+=1
            else:
                stack[-1] = 1
                while i < len(s) and s[i] == ')':
                    x = stack.pop()
                    stack[-1]+=2*x
                    i+=1
                
            
        return int(stack[-1]/2)
        
                
                
            
        
        
        
        