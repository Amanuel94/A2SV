class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        paths = []

        def dfs(graph, node, n, cur):
            nonlocal paths
            # print(cur)
            if node == (n-1):
                paths.append(cur[:])

            for nbr in graph[node]:
                cur.append(nbr)
                dfs(graph, nbr, n, cur)
                cur.pop()

        dfs(graph, 0, len(graph), [0])

        return paths