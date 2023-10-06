class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        graph = defaultdict(list)
        for i, edge in enumerate(edges):
            u, v  = edge
            graph[u].append([succProb[i], v])
            graph[v].append([succProb[i], u])
        
        heap = [(-1, start)]
        seen = [0]*n

        while heap:
            prod, node = heappop(heap)
            if node == end:
                return -prod
            if seen[node]:
                continue
            seen[node] = 1

            for prob, nbr in graph[node]:
                print(node, nbr, seen[nbr])
                if seen[nbr] == 0:
                    heappush(heap, (prod*prob, nbr))
                    
        return 0