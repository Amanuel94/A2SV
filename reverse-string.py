class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        n = len(s)-1
        while i < n/2+1:
            s[i], s[n - i] = s[n - i], s[i]
            i+=1
