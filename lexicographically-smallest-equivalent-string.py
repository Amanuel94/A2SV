class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        p = {chr(i):chr(i) for i in range(97, 97+26)}
        def getP(c):
            if p[c] == c:
                return c
            p[c] =  getP(p[c])
            return p[c]
        i = 0
        while i < len(s1):
            x, y =  getP(s1[i]), getP(s2[i])
            if x < y:
                p[y] = x
            else:
                p[x] = y
            i+=1
        ans = ""
        for i in baseStr:
            ans+=getP(i)
        return ans