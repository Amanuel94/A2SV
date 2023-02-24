class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        d = {')':'(',']':'[', '}':'{'}
        i = 0
        for i, p in enumerate(s):
            if p in d.values():
                stack.append(p)
            elif stack and stack[-1] == d[p]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True
            
            
        