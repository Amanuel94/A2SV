class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        stones.sort()
        p = {i:i for i in range(len(stones))}
        X = defaultdict(list)
        Y = defaultdict(list)
        size = [0]*len(stones)

        def getP(i):
            if i == p[i]:
                return i
            p[i] = getP(p[i])
            return p[i]
        
        for ind, stone in enumerate(stones):
            x, y = stone
            if X[x]:
                p[p[ind]] = getP(X[x][0])

            if Y[y]:
                p[p[ind]] = getP(Y[y][0])

            X[x].append(ind)
            Y[y].append(ind)


        ans = 0
        print(p)
        for i in range(len(stones)):
            par = getP(i)
            if par != i:
                size[par]+=1
        

        return sum(size)