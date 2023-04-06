from collections import defaultdict
graph = defaultdict(list)
n  = int(input())

for _ in range(n):
    for i, deg in enumerate(map(int, input().split())):

        if deg:
            graph[_+1].append(i+1)

for u in graph:

    print(len(graph[u]), end = ' ')
    print(*graph[u])
