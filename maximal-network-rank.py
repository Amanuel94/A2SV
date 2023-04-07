class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        
        degs = defaultdict(int)
        connected = defaultdict(int)
        
        for road in roads:
            
            degs[road[0]]+=1
            degs[road[1]]+=1
            
            connected[tuple(road)] = 1
             
            
            
        max_rank = 0
        
        for u in range(n):
            for v in range(n):
                
                if u!=v:
                    if connected[(u,v)] or connected[(v, u)]:
                        max_rank = max(max_rank, degs[u]+degs[v]-1)
                    else:
                        max_rank = max(max_rank, degs[u]+degs[v])
        
        return max_rank
