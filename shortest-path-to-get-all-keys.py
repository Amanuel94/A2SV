class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:

        keys_ = 127
        n = len(grid)
        m = len(grid[0])
        start = None
        for i in range(n):
            for j in range(m):
                ind = ord(grid[i][j]) - 65
                if 0 <= ind <= 5:
                    keys_ &= ~(1<<ind)
                elif grid[i][j] == '@':
                    start = [i,j]
                    # grid[i] = grid[i][:j] + '.' + grid[i][j+1:] 

        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        count = -1
        # print(bin(keys_))
        start = tuple(start + [keys_])
        q = deque([start])
        v = set([start])
        def inBound(i, j):
            return 0<=i<len(grid) and 0<=j<len(grid[0])
        while q:
            lvl = len(q)
            count+=1
            # print(q, v)
            for _ in range(lvl):
                x, y, keys = q.popleft()
                if 0 <= ord(grid[x][y])-97 <= 5:
                    i = ord(grid[x][y])-97
                    keys|= (1<<i)

                if keys == 127:
                    return count
                for dx, dy in directions:
                    tx, ty = x+dx, y+dy
                    if inBound(tx, ty) and 0<= ord(grid[tx][ty])-65 < 6 and (tx, ty, keys) not in v:
                        if keys>>(ord(grid[tx][ty])-65)&1:
                            q.append((tx,ty,keys))
                            v.add((tx, ty, keys))
                    elif inBound(tx, ty) and grid[tx][ty] in [ '@', '.'] and (tx, ty, keys) not in v:
                        q.append((tx, ty, keys))
                        v.add((tx, ty, keys))
                    elif inBound(tx, ty) and 0<= ord(grid[tx][ty])-97 < 6 and (tx, ty, keys) not in v:
                        q.append((tx, ty, keys))
                        v.add((tx, ty, keys))
        return -1