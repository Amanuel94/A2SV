class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = {i:i for i in range(n)}

        def par(node):
            while node!=graph[node]:
                node= graph[node]
            return node

        
        vis = set()
        for u,v in edges:
            if v in vis:
                u, v = v, u
            graph[par(v)]=  par(u)
            vis.add(u)
            vis.add(v)
        
        return par(source) == par(destination)