class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # self.matrix = matrix
        self.res = [[0] * (len(matrix[0]) + 1)]
        
        for i in range(len(matrix)):
            pre = [0]
            for j in range(len(matrix[0])):
                pre.append(pre[-1] + matrix[i][j] + self.res[-1][j + 1] - self.res[-1][j])
                
            self.res.append(pre)
            
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        
        return self.res[row2 + 1][col2 + 1] - self.res[row2 + 1][col1] - self.res[row1][col2 + 1] + self.res[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)