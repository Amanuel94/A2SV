class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        grid_T = self.transpose(grid)
        ans = 0
        for i, row in enumerate(grid):
            for col in grid_T:
                
                if col == row:
                    ans+=1
        return ans 

    def transpose(self, matrix):
        tr = [[0]*len(matrix) for i in range(len(matrix[0]))]
        for i, row in enumerate(matrix):
            for j in range(len(tr)):
                tr[j][i] = row[j]
        return tr
