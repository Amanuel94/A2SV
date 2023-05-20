class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        p = {(i+1,j+1):(i+1,j+1) for i in range(row) for j in range(col)}
        def getP(node):
            if node == p[node]:
                return node
            p[node] = getP(p[node])
            return p[node]
        span = defaultdict(set)
        directions =  [(1, 0), (0, 1), (0,-1), (-1,0), (1,1), (1,-1),(-1,1),(-1,-1)]
        # def inBound(i, j):
        #     return 0 <= i < row and 0 <= j < col

        oned = set()
        for i, cell in enumerate(cells):
            x, y  = cell
            for dx, dy in directions:
                tx, ty = x+dx, y+dy
                span[getP((x, y))].add(y)
                if (tx, ty) in oned:
                    span[getP((tx,ty))].update(span[getP((x, y))])

                    p[getP((x, y))] = getP((tx, ty))
                if len(span[getP((x, y))]) == col:
                    return i
            oned.add((x,y))
        return len(cells)-1