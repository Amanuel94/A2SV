class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        graph = defaultdict(list)
        counter = defaultdict(list)
        count = defaultdict(int)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        ans = [0]*n
        
        def dfs(node, vis):
            vis.add(node)
            counter = defaultdict(int)
            for nbr in graph[node]:
                if nbr not in vis:
                    temp = dfs(nbr, vis)
                    for k in temp:
                        counter[k]+= temp[k]
            counter[labels[node]]+=1
            ans[node] = counter[labels[node]]

            return counter

        dfs(0, set())
    
        return ans