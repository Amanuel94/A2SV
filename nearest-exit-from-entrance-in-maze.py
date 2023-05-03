class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        q = deque([tuple(entrance)])
        vis = set([tuple(entrance)])
        directions = [(1,0), (0, 1), (-1,0), (0,-1)]
        count = -1
        n = len(maze)
        m = len(maze[0])

        while q:
            lvl = len(q)
            count+=1
            for _ in range(lvl):
                i, j = q.popleft()
                if i == 0 or i == n-1 or j == 0 or j== m-1:
                    if [i, j] != entrance:
                        return count
                for x, y in directions:
                    if 0<= i+x< n and 0<= j+y < m and (i+x, j+y) not in vis and maze[i+x][j+y] != '+':
                        q.append((i+x, j+y))
                        vis.add((i+x, j+y))
        return -1