class Solution(object):
    def spiralOrder(self, matrix):
        if len(matrix) > 1:
            first_row = matrix[0]
            matrix = matrix[1:]
            return first_row + self.spiralOrder(self.rotateMatrix(matrix))
        else:
            return matrix[0]
    
    def rotateMatrix(self, matrix):
        rotated = []
        m = len(matrix)
        n = len(matrix[0])
        
        for i in xrange(n):
            row = [matrix[k][n-i-1] for k in range(m)]
            rotated.append(row)
        return rotated
