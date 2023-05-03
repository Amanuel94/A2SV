class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        vis = set()
        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        island1 = []
        n, m = len(grid), len(grid[0])
        i = 0
        while i < n:
            j = 0
            f = False
            while j < m:
                if grid[i][j] == 1:
                    f = True
                    break
                j+=1
            if f:
                break
            i+=1
        def dfs(node):
            vis.add(node)
            x, y = node
            grid[x][y] = 0
            for dx,dy in directions:
                if (x+dx, y+dy) not in vis and 0<= x+dx< n and 0<=y+dy< m and grid[x+dx][y+dy] == 1:
                    dfs((x+dx, y+dy))
        dfs((i,j))
        q = deque(vis)
        count = -2
        while q:
            lvl = len(q)
            count+=1
            for _ in range(lvl):
                x, y = q.popleft()
                if grid[x][y] == 1:
                    return count
                for dx, dy in directions:
                    if (x+dx, y+dy) not in vis and 0<= x+dx< n and 0<=y+dy< m:
                        q.append((x+dx, y+dy))
                        vis.add((x+dx, y+dy))