class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        # image = img[:]
        visited = set()
        def dfs(color, i, j, start,visited):
            
            # i, j = pos
            image[i][j] = color
            # print(i, j, image)
            visited.add((i, j))
            for dir_ in directions:
                x, y = dir_
                a, b = i+x, j+y
                
                if (a, b) not in  visited and 0<= a< len(image) and 0 <=b < len(image[0]) and image[a][b] == start:
                    dfs(color, a,b, start, visited)
                
            return
        dfs(color,sr, sc, image[sr][sc], visited)
        return image