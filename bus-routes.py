class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source ==  target:
            return 0
        carrier = defaultdict(list)
        graph = defaultdict(list)
        for i, route in enumerate(routes):
            for station in route:
                for s in carrier[station]:
                    graph[s].append(i)
                    graph[i].append(s)
                carrier[station].append(i)
        que = deque(carrier[source])
        vis = set(carrier[source])
        target = set(carrier[target])
        count = 0
        while que:
            count+=1
            level = len(que)
            for _ in range(level):
                cur = que.popleft()
                if cur in target:
                    return count
                for nbr in graph[cur]:
                    if nbr not in vis:
                        que.append(nbr)
                        vis.add(nbr)
        return -1