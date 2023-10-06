class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)
        
        for i, equation in enumerate(equations):
            u, v = equation
            graph[u].append([v, values[i]])
            graph[v].append([u, 1/values[i]])
        
        ans = []
        for q_num, q_den in queries:
            if q_num not in graph or q_den not in graph:
                ans.append(-1)
                continue

            not_found = 1
            queue = deque([[q_num, 1]])
            seen = set([q_num])

            while queue:
                node, prod = queue.popleft()
                if node == q_den:
                    ans.append(prod)
                    not_found = 0
                    break

                    
                for nbr, val in graph[node]:
                    if nbr not in seen:
                        queue.append([nbr, val*prod])
                        seen.add(nbr)
            if not_found:
                ans.append(-1)
            # print(q_num, q_den, ans)
        return ans