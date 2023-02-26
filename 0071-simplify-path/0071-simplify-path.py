class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        arr = path.split('/')
        
        stack = []
        
        for i in arr:
            if i in ['.', '']:
                continue
            elif i == '..' and stack:
                stack.pop()
            elif i == '..':
                continue
            else:
                stack.append(i)
        return "/" + "/".join(stack)
        