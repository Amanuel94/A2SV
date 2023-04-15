class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        count = 0

        def dfs(grid2, grid1, i, j):
            ans  = True
            if grid1[i][j] == 0:
                ans = False
            grid2[i][j] = 0

            for dir_ in directions:
                a, b = dir_
                if 0 <= a+i < len(grid1) and  0 <= b+j < len(grid1[0]) and grid2[i+a][j+b] == 1:
                    ans = dfs(grid2, grid1, i+a, j+b) and ans
                        
            return ans



        for i, row in enumerate(grid2):
            for j, cell in enumerate(row):
                if cell and dfs(grid2, grid1, i, j):
                    count+=1
        return count