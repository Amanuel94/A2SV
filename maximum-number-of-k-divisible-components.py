class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        valSums = [0]*n

        seen = [0]*n
        def makeValSums(root, k):
            seen[root] = 1
            valSums[root]
            for nbr in graph[root]:
                if seen[nbr] == 0:
                    valSums[root]+=makeValSums(nbr, k)
            valSums[root]+=values[root]
            valSums[root]%=k
            return valSums[root]

        makeValSums(0, k)
        return len([i for i in range(n) if valSums[i] == 0])