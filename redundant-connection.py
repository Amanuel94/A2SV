class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        p = {i+1:i+1 for i in range(len(edges))}

        def getParent(i):
            if i == p[i]:
                return i
            s = getParent(p[i])
            p[i] = s
            return s
    
        for u, v in edges:
            if getParent(u) == getParent(v):
                return [u, v]
            p[getParent(v)] = u