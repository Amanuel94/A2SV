class Solution(object):
    def rotate(self, matrix):
        d_sum = 0
        n = len(matrix)
        while d_sum < 2*n - 1:
            i = max(0, d_sum-n+1)
            while i < d_sum-i:
                matrix[i][d_sum-i],matrix[d_sum-i][i] = matrix[d_sum-i][i],matrix[i][d_sum-i]
                i+=1
            d_sum+=1
            
        i = 0
        while i < n:
            j = 0
            while j < n/2:
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j],matrix[i][j]
                j+=1
            i+=1
        
                
            
            
        
                
            
        
        