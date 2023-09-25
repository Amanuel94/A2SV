class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:

        graph = defaultdict(list)
        # adjacent = defaultdict(set)

        # construct graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        cost =  [0]*n
        # do dfs
        def dfs(prev, src, dest):
            
            cost[src]+=1
            if src == dest:
                return True
            for nbr in graph[src]:
                if nbr != prev:
                    if dfs(src, nbr, dest):
                        return True
            cost[src]-=1
            return False

        for src, dest in trips:
            dfs(None, src, dest)
        
        cost = list(map(lambda x: price[x]*cost[x]//2, range(n)))
        total_cost = sum(cost)*2

        # @cache
        # def dp(node, prev, isPicked):
            
        #     ans_picked = 0
        #     ans_not_picked = 0

        #     if isPicked:
        #         for nbr in graph[node]:
        #             if nbr != prev:
        #                 ans_picked+=dp(nbr, node, False)
        #     else:
        #         ans_not_picked = cost[node]
        #         for nbr in graph[node]:
        #             if nbr != prev:
        #                 ans_not_picked+=max(dp(nbr, node, False), dp(nbr, node, True))
        #             if node == 1:
        #                 print(ans_not_picked)

        #     return max(ans_picked, ans_not_picked)

        @cache
        def dp(node, prev, isPicked):

            ans_not_picked = 0
            if not isPicked:
                ans_not_picked = cost[node]
                for nbr in graph[node]:
                    if nbr != prev:
                        ans_not_picked += dp(nbr, node, True)

            ans_picked = 0
            for nbr in graph[node]:
                if nbr != prev:
                    ans_picked += dp(nbr, node, False)
                    
            return max(ans_picked, ans_not_picked)

      
        return total_cost - dp(0, None, False)