class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        graph =  defaultdict(list)
        toVis =  list(range(len(bombs)))
        for i, pos1 in enumerate(bombs):
            x1, y1, r1 = pos1
            for j, pos2 in enumerate(bombs):
                x2, y2, r2 = pos2
                if i!=j and (x2- x1)*(x2- x1) + (y2- y1)*(y2- y1) <= r1*r1:
                    graph[i].append(j)
        # print(graph)
        def dfs(node, vis):
            nonlocal toVis, graph
            count = 0
            vis.add(node)
            # toVis.remove(node)

            for nbr in graph[node]:
                if nbr not in vis:
                    count+= dfs(nbr, vis)
            return count+1
        ans = 0
        for node in range(len(bombs)):
            ans =  max(dfs(node, set()), ans)

        return ans