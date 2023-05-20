class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        vis = set()
        graph = defaultdict(list)
        pre = defaultdict(set)
        
        for u, v in edges:
            graph[v].append(u)

        def dfs(node):

            vis.add(node)
            
            for nbr in graph[node]:
                if nbr not in vis:
                    dfs(nbr)
                pre[node].add(nbr)
                pre[node]|=pre[nbr]


        res = []
        for node in range(n):
            if node not in vis:
                dfs(node)
        for u in range(n):
            res.append(sorted(list(pre[u])))
        return res