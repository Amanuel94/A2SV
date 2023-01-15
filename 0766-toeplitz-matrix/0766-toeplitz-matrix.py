class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        d_diff = len(matrix)-1

        
        while d_diff > -len(matrix[0]):
            i = max(0, d_diff)
            c = matrix[i][i - d_diff]

            while i < len(matrix) and i - d_diff < len(matrix[0]):
                if c != matrix[i][i-d_diff]:
                    return False
                i+=1
            d_diff-=1
        return True
    
        