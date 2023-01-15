class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m= len(mat)
        n = len(mat[0])
        
        if m*n != r*c:
            return mat
        
        
        reshaped = [[0]*c for i in range(r)]
        for i, row in enumerate(mat):
            for j, cell in enumerate(row):
                
                # flatten mat and reshape the flattened array into rxc array
                reshaped[(i*n + j)//c][(i*n + j)%c] = cell
                
        return reshaped
        
        