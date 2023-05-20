class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        p = {i:i for i in range(1, n+1)}
        min_= {i:float('inf') for i in range(1, n+1)}

        def getP(i):
            if p[i] == i:
                return i
            p[i] = getP(p[i])
            return p[i]

        for a, b, dist in roads:
            a, b = getP(a), getP(b)
            p[b] = a
            min_[a] = min(min_[b], min_[a], dist)
            

        return min_[getP(1)]