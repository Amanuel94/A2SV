class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        vis = set()
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        
        start = 0
        for key in graph:
            if len(graph[key]) == 1:
                start = key
                break

        order = []

        def dfs(node):
            vis.add(node)
            for nbr in graph[node]:
                if nbr not in vis:
                    dfs(nbr)
            order.append(node)
        dfs(start)
        return order