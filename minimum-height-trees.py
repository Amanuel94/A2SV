class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n < 2:
            return [0]

        inc1 = [0]*n
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            inc1[u]+=1
            inc1[v]+=1

        q1 = deque([i for i in range(n) if inc1[i] == 1])
        order1 = []
        ans = 0
        while q1:
            x = q1.popleft()
            order1.append(x)
            for nbr in graph[x]:
                inc1[nbr]-=1
                if inc1[nbr] == 1:
                    q1.append(nbr)
        d1 = self.checkDepth(order1[-1], graph, set(), 0)
        d2 = self.checkDepth(order1[-2], graph, set(), 0)
        if d1 == d2:
            return [order1[-1], order1[-2]]
        else:
            return [order1[-1]]
     
        
    def checkDepth(self, node, graph, vis, depth):
        vis.add(node)
        ans = depth
        for nbr in graph[node]:
            if nbr not in vis:
                ans = max(ans, self.checkDepth(nbr, graph, vis, depth+1))
        return ans