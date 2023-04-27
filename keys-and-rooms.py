class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = set([0])
        # toVis = set(range(len(rooms)))
        que = deque([0])

        while que:
            cur = len(que)
            for _ in range(cur):
                for nbr in rooms[que.popleft()]:
                    if nbr not in visited:
                        que.append(nbr)
                        # toVis.discard(nbr)
                        visited.add(nbr)
        return len(visited) == len(rooms)