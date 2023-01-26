class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        
        
        
        def trans(b):
            return [[b[i][j] for i in range(3)] for j in range(3)]
        
        def winner(board, s):
            if [s]*3 in board:
                return True
            elif [s]*3 in trans(board):
                return True
            elif board[0][0] == s and board[1][1] == s and board[2][2] == s:
                return True
            elif board[0][2] == s and board[1][1] == s and board[2][0] == s:
                return True
            else:
                return False

        board = list(map(list, board))
        # print(board)
        
        X = 0
        O = 0
        
        # print(trans(board))
        
        for row in board:
            for cell in row:
                X+= int(cell == 'X')
                O+= int(cell == 'O')
        if O > X:
            return False
        elif X - O >= 2:
            return False
        elif winner(board, 'X') and winner(board, 'O'):
            return False
        elif winner(board, 'X') and X == O:
            return False
        elif winner(board, 'O') and X > O:
            return False
        
        
        return True
 