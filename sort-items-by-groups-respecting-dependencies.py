class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        start = {}
        groups = defaultdict(set)
        for i, g in enumerate(group):
            if g == -1:
                group[i] = m
                start[m] = i
                groups[m].add(i) 
                m+=1
            else:
                groups[g].add(i)
                           
     
        gr = [defaultdict(list) for i in range(m)]
        ref = [[] for i in range(m)]
        ans = []
        inc = [0]*m
        col = defaultdict(int)
        

        for i, befores in enumerate(beforeItems):
            for before in befores:
                if group[before] == group[i]:
                    gr[group[i]][before].append(i)
                else:
                    ref[group[before]].append(group[i])
                    inc[group[i]]+=1

        res = []
        order = []
        q = deque([i for i in range(m) if inc[i] == 0])
        while q:
            x = q.popleft()
            order.append(x)
            for nbr in ref[x]:
                inc[nbr]-=1
                if inc[nbr] == 0:
                    q.append(nbr)
        if sum(inc):
            return []

        # def bfs(i, q):
        #     ans = []
        #     while q:
        #         x = q.popleft()
        #         ans.append(x)
        #         for nbr in gr[i][x]:
        #             inc_g[i][nbr]-=1
        #             if inc_g[i][nbr] == 0:
        #                 q.append(nbr)
        #     return ans
        ans = []
        def dfs(node, i):
            col[node] = 1
            for nbr in gr[i][node]:
                if col[nbr] == 1:
                    return False
                elif col[nbr] == 0:
                    if not dfs(nbr, i):
                        return False
            ans.append(node)
            col[node] = 2
            return True
            
                        

        # print(order,start, dict(groups), dict(gr[0]))
        for i in order:
            if i in start:
                res.append(start[i])
            else:
                # print(i, j)
                a = []
                for j in groups[i]:
                    if col[j] == 0:
                        s = dfs(j, i)
                        if not s:
                            return []
                        else:
                            a.extend(ans)
                            ans = []
                res.extend(a[::-1])
            
        return res