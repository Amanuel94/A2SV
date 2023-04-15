from collections import defaultdict


while True:
    n = int(input())

    if n == 0:
        break
    l = int(input())

    graph = defaultdict(list)
    color = defaultdict(int)
    for _ in range(l):
        u, v = list(map(int, input().split()))
        root = u
        graph[u].append(v)
        graph[v].append(u)
        color[u] = 2
        color[v] = 2


    def dfs(graph, node, vis, col):
        vis.add(node)
        color[node] = col

        ans = True

        for nbr in graph[node]:
            if color[nbr] == col:
                return False
            elif nbr not in vis:
                ans =  ans and dfs(graph, nbr, vis, 1-col)
        return ans

    if l == 0:
        print('BICOLOURABLE.')
    elif dfs(graph, root, set(), 0):
        print('BICOLOURABLE.')
    else:
        print('NOT BICOLOURABLE.')
