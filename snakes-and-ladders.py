class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        choices = [1,2,3,4,5,6]
        n = len(board)
        count = -1
        q = deque([1])
        vis = set([1])

        def nToGrid(k, n):
            i = n - ((k-1)//n)
            j = (k-1)%n
            if (n - i)%2:
                j = n - 1 - j
            return i-1, j

        while q:
            lvl = len(q)
            count+=1
            print(q)
            for _ in range(lvl):
                cur = q.popleft()
                if cur >= n*n:
                    return count
                for choice in choices:
                    x, y = nToGrid(min(cur + choice, n*n), n)
                    if cur+choice not in vis:
                        if board[x][y] == -1:
                            q.append(cur+choice)
                            
                        else:
                            q.append(board[x][y])

                        vis.add(cur+choice)
        return -1