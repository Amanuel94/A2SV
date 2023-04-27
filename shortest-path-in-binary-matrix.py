class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1:
            return -1

        directions = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
        vis = set([(0,0)])
        que = deque([(0,0)])
        n =  len(grid)
        node = (0,0)
        count = 0

        def in_bound(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid)

        while que:
            count+=1
            cur_len = len(que)
            for _ in range(cur_len):
                i, j = que.popleft()
                if i == n-1 and j == n-1:
                    return count
                for x, y in directions:
                    if in_bound(i+x, j+y) and grid[i+x][j+y] == 0 and (i+x, j+y) not in vis: 
                        que.append((i+x, j+y))
                        vis.add((i+x, j+y))
                

        return -1