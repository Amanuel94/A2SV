class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        col = defaultdict(int)
        nodes = list(range(1, n+1))
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
            col[u] = 2
            col[v] = 2

        while nodes:
            if not self.dfs(graph, nodes[0], set(), 0, col, nodes):
                return False
        return True
            

        

        

    def dfs(self, graph, node, visited, col, colors, toVis):

        for nbr in graph[node]:
            if colors[nbr] == col:
                return False
        visited.add(node)
        toVis.remove(node)
        colors[node] = col

        ans = True
        for nbr in graph[node]:
            if nbr not in visited:
                ans =  ans and self.dfs(graph, nbr, visited, 1-col, colors, toVis)
        return ans