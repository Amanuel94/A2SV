class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        n = len(grid)
        par = {(i, j):(i, j) for i in range(n) for j in range(n)}
        size = {(i, j): 1 for i in range(n) for j in range(n)}


        def getP(coord):
            if par[coord] == coord:
                return coord
            par[coord] = getP(par[coord])
            return par[coord]

        def inBound(i, j, n):
            return 0 <= i < n and 0 <= j < n

        dir = [(1,0), (0,1), (-1,0), (0, -1)]
        ans = 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    for dx, dy in dir:
                        tx, ty = i + dx, j + dy
                        if inBound(tx, ty, n) and grid[tx][ty] == 1 and getP((i,j))!= getP((tx, ty)):
                            size[getP((i, j))]+=size[getP((tx, ty))]
                            ans = max(ans, size[getP((i, j))])
                            par[getP((tx, ty))] = getP((i, j))
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neis = set()
                    for dx, dy in dir:
                        tx, ty = i + dx, j + dy
                        if inBound(tx, ty, n) and grid[tx][ty] == 1:
                            neis.add(getP((tx, ty)))
                    cur = 1
                    for nei in neis:
                        cur+=size[nei]
                    ans=  max(ans, cur)
        return ans