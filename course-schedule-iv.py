class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        vis = set()
        graph = defaultdict(list)
        pre = defaultdict(set)
        
        for u, v in prerequisites:
            graph[u].append(v)

        def dfs(node):
    
            
            vis.add(node)
            pre[node].add(node)
            for nbr in graph[node]:
                if nbr not in vis:
                    dfs(nbr)
                pre[node]|=pre[nbr]


        res = []
        # print(dict(pre))
        for node in range(numCourses):
            if node not in vis:
                dfs(node)
        for u, v in queries:
            res.append(v in pre[u])
        return res