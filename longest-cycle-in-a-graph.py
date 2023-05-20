class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        col = defaultdict(int)
        starts = [i for i in range(len(edges)) if edges[i] >0]
        ans = -1
        vis = set()
        def dfs(node, prev):
            nonlocal ans
            col[node] = prev
            
            if edges[node] >= 0 and col[edges[node]] > 0 and edges[node] not in vis:
                ans = max(ans, prev+1 - col[edges[node]])
                
            elif edges[node] >= 0 and col[edges[node]] == 0 and edges[node] not in vis:
                dfs(edges[node], prev+1)
                    
            vis.add(node)

        for start in starts:

            dfs(start, 1)
            # print(start, vis)
            # col = defaultdict(int)
            
        return ans