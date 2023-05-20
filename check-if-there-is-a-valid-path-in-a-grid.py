class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        graph = {(i, j):(i,j) for i in range(len(grid)) for j in range(len(grid[0]))}     
        directions = [(1,0),(0,1), (-1,0),(0,-1)]
        q = deque([(0,0)])
        vis = set([(0,0)])

        compat = {
            1:[[],[1,3,5],[],[1,4,6]],
            2:[[2,5,6],[],[2,3,4],[]],
            3:[[2,5,6],[],[],[1,4,6]],
            4:[[2,5,6],[1,3,5],[],[]],
            5:[[],[],[2,3,4],[1,4,6]],
            6:[[],[1,3,5],[2,3,4],[]],
        }

        def par(x):
            node = x
            while node != graph[node]:
                node = graph[node]
            # while node != x:
            #     graph[x] = node
            #     x = node
            return node

        def inBound(i,j):
            return 0 <= i < len(grid) and 0<=j<len(grid[0])


        while q:
            x, y = q.popleft()
            cur = grid[x][y]
            for i, tup in enumerate(directions):
                dx,dy = tup
                if inBound(x+dx, y+dy) and (x+dx, y+dy) not in vis:
                    next = grid[x+dx][y+dy]
                    if next in compat[cur][i]:
                        vis.add((x+dx, y+dy))
                        q.append((x+dx, y+dy))
                        graph[par((x+dx, y+dy))] = par((x,y))

        return par((0,0)) == par((len(grid)-1, len(grid[0])-1))