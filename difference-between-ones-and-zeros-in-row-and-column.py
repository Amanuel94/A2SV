class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        # ones_zeros(grid) is a 1 dimensional list such that ones_zeros(grid)[i] = the number of ones - number of zero in the i-th row of grid
        grid_sum = self.ones_zeros(grid)
        grid_sum_tr = self.ones_zeros(self.transpose(grid))

        res = []
        
        for sum_1 in  grid_sum:
            sum_row = []
            
            for sum_2 in grid_sum_tr:
                sum_row.append(sum_1 + sum_2)
                
            res.append(sum_row)

        return res

    def ones_zeros(self, grid):

        mat = []

        for row in grid:
            mat.append(2*sum(row) - len(row))

        return mat


    def transpose(self, matrix):
        tr = [[0]*len(matrix) for i in range(len(matrix[0]))]
        for i, row in enumerate(matrix):
            for j in range(len(tr)):
                tr[j][i] = row[j]
        return tr





        
            


        
