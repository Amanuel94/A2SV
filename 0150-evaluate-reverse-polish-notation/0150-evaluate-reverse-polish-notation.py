class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            
            if token in ["+", "-", "*", "/"]:
                x = stack.pop()
                y = stack.pop()
                    
                ans =  str(eval(y + token + x)).split('.')
                stack.append(ans[0] + ".0")
            else:
                stack.append(token+ ".0")
                
        return int(float(stack[-1]))
            
                    
        