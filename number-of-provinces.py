class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i, row in enumerate(isConnected):
            for j, col in enumerate(row):
                if col and i!=j:
                    adj[i].append(j)
                    adj[j].append(i)

        toVis = list(range(len(isConnected)))
        # print(adj, toVis)
        count = 0

        while toVis:
            self.dfs(toVis[0], set(), adj, toVis)
            count+=1
        return count


    def dfs(self, node, visited, adj, toVis):

        visited.add(node)
        toVis.remove(node)
        for neighbour in  adj[node]:
            if neighbour not in visited:
                self.dfs(neighbour, visited, adj, toVis)