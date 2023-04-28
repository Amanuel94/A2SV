class Solution:
    def updateMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        que = deque()
        vis = set()
        ans = [[0]*len(grid[0]) for _ in range(len(grid))]
        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        count = 0
        
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 0:
                    que.append((i,j))
                else:
                    ans[i][j] = float('inf')
        def inBound(i,j):
            return 0<=i< len(grid) and 0 <= j < len(grid[0])
        
        while que:
            count+=1
            cur_level = len(que)
            for _ in range(cur_level):
                z1, z2 = que.popleft()
                for x, y in directions:
                    if inBound(z1+x, z2+y) and (z1+x, z2+y) not in vis and grid[z1+x][z2+y] == 1:
                        ans[z1+x][z2+y] = min(ans[z1+x][z2+y], count)
                        que.append((z1+x, z2+y))
                        vis.add((z1+x, z2+y))
        return ans