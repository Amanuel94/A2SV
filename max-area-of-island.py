class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        graph = defaultdict(list)
        nodes= []
        ans = 0
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if grid[i][j] == 1:
                    nodes.append((i,j))
                    if i > 0 and grid[i-1][j]:
                        graph[(i, j)].append((i-1, j))
                    if i < len(grid)-1 and grid[i+1][j]:
                        graph[(i, j)].append((i+1, j))
                    if j > 0 and grid[i][j-1]:
                        graph[(i, j)].append((i, j-1))
                    if j < len(grid[0])-1 and grid[i][j+1]:
                        graph[(i, j)].append((i, j+1))

        # print(nodes)
        while nodes:
            ans = max(ans, self.dfs(nodes[0], set(), graph, nodes))

        return ans


        
    def dfs(self, node, visited, graph, nodes):
        count = 0
        nodes.remove(node)
        visited.add(node)

        for nbr  in graph[node]:
            if nbr not in visited:
                count+=self.dfs(nbr, visited, graph, nodes)
        return count+1