class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        # create tree
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # traverse and count
        def max_depth(node, vis):
            vis.add(node)
            ans = -1
            
            for nbr in graph[node]:
                if nbr not in vis:
                    cur = max_depth(nbr, vis)
                    if cur != -1:
                        ans = max(ans, 0)
                        ans+= (cur + 2)
            # print(node, ans)
            if hasApple[node]:
                # print(node, ans)
                return max(0, ans)
            else:
                
                return ans

        return max(max_depth(0, set()), 0)