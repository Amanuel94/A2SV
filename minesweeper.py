class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1)
        ]

        def inBound(x,y):
            return 0 <=  x < len(board) and 0<=y <len(board[0])

        
        def reveal(click, vis):
            nonlocal board
            r, c = click
            vis.add((r,c))
            if board[r][c] == 'M':
                board[r][c] = 'X'
                
            elif board[r][c] == 'E':
                adj = 0
                for dir_ in directions:
                    x, y = dir_
                    if inBound(x+r, y+c) and board[x+r][y+c] == 'M':
                        adj+=1
                if adj:
                    board[r][c] = str(adj)
                else:
                    for dir_ in directions:
                        x, y = dir_
                        if (x+r, c+y) not in vis and inBound(x+r, y+c):
                            reveal([x+r, c+y], vis)
                    board[r][c] = 'B'


        reveal(click, set())

        return board