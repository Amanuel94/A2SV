class Solution(object):
    def findTheDifference(self, s, t):
        s, t = sorted(list(s)), sorted(list(t))

        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]
