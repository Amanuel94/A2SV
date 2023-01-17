class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell == 0:
                    zeros.append((i, j))
                    
        for tup in zeros:
            matrix[tup[0]] = [0]*len(matrix[0])
            for i, row in enumerate(matrix):
                matrix[i][tup[1]] = 0
                
            

                    
        