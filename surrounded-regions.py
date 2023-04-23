class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        directions = [(1,0),(0,1), (0,-1), (-1, 0)]
        cmp_grid = copy.deepcopy(grid)
        def inbound(i, j):
            return 0<=i<len(grid) and  0 <= j < len(grid[0])
        
        def dfs(i, j):
            cmp_grid[i][j] = 'X'
            for x, y in directions:
                if inbound(i+x, j+y) and cmp_grid[i+x][j+y] == 'O':
                    dfs(i+x, j+y)

                        
        for i in [0, len(grid)-1]:
            j = 0
            while j < len(grid[0]):
                if cmp_grid[i][j] == 'O':
                    dfs(i, j)
                j+=1
        for i in [0, len(grid[0])-1]:
            j = 0
            while j < len(grid):
                if cmp_grid[j][i] == 'O':
                    dfs(j, i)
                j+=1

        i = 0
        while i < len(grid):
            j = 0
            while j < len(grid[0]):
                if cmp_grid[i][j] == grid[i][j]:
                    grid[i][j] = 'X'
                else:
                    grid[i][j] = 'O'
                j+=1
            i+=1