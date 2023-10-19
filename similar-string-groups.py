class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        n = len(strs)
        p = {i:i for i in range(n)}
        
        def getP(i):
            if i == p[i]:
                return i
            p[i] = getP(p[i])
            return p[i]
    
        for i in range(n):
            wi = strs[i]
            for j in range(i+1, n):
                wj = strs[j]
                diff = 0
                for k in range(len(wi)):
                    diff+=int(wi[k] != wj[k])
                    if diff >= 3:
                        break
                else:
                    p[getP(j)] = getP(i)
        # print(p)
        for _ in range(n):
            getP(_)
        return len(set(p.values()))