class Solution(object):
    def maxSum(self, mat):
        m = len(mat)
        n = len(mat[0])
        res = 0
        for j in range(n-2):
            for i in range(m-2):
                        wind1 = sum(mat[i][j:j+3])
                        wind2 = mat[i+1][j+1]
                        wind3 = sum(mat[i+2][j:j+3])
                        res = max(wind1+wind2+wind3, res)
        return res
