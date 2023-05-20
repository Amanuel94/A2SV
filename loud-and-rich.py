class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int])  -> List[int]:

        graph = defaultdict(list)
        vis = set()
        for a, b in richer:
            graph[b].append(a)
        res = [0]*len(quiet)
        def dfs(node):
            min_ = quiet[node]
            ans = node
            for nbr in graph[node]:
                if nbr not in vis:
                    m = dfs(nbr)
                    if  quiet[m] < min_:
                        min_ = quiet[m]
                        ans = m 
                else:
                    m = res[nbr]
                    if  quiet[m] < min_:
                        min_ = quiet[m]
                        ans = m 

            vis.add(node) 
            res[node] = ans
            return ans
        for i in range(len(quiet)):
            if i not in vis:
                dfs(i)
        return res