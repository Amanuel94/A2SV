class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        inc = defaultdict(int)
        
        for i, row in enumerate(graph):
            for j, cel in enumerate(row):
                adj[cel].append(i)
                inc[i]+=1
                
        q = deque([i for i in range(len(graph)) if inc[i]==0])
        # print(q)
        while q:
            x = q.popleft()
            for nbr in adj[x]:
                inc[nbr] -=1
                if inc[nbr] == 0:
                    q.append(nbr)
        return [i for i in range(len(graph)) if inc[i] == 0]