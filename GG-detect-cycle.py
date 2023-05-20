from typing import List
from collections import defaultdict
class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        #Code here
        col = defaultdict(int)
        def dfs(node, prev):
            col[node] =  1
            for nbr in adj[node]:
                if col[nbr] == 1 and nbr != prev:
                    return False
                elif col[nbr] != 1:
                    if not dfs(nbr, node):
                        return False
            col[node] = 2
            return True
        for i in range(len(adj)):
            if col[i] == 1 or not dfs(i, None):
                return True
        return False
              
                        
           
            

