class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for i, row in enumerate(board):
            if not self.check_list(row):
                return False
            if not self.check_list([r[i] for r in board]):
                return False
            if not self.check_list([board[j//3 + 3*(i//3)][j%3 + (3*i)%9] for j in range(9)]):
                return False
        return True
        
    def check_list(self, row):
        counter = []
        for num in row:
            if num in counter:
                return False
            elif num != '.':
                counter.append(num)
        return True
    