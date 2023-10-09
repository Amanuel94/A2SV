from bisect import bisect_left
from heapq import heappop, heappush
from collections import defaultdict
import sys

input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        ladders = [[] for _ in range(n)]
        floors = [set() for _ in range(n)]
        x = list(map(int, input().split()))

        for _ in range(k):
            a, b, c, d, h = map(int, input().split())
            ladders[a - 1].append((b - 1, c - 1, d - 1, h))
            floors[a - 1].add(b - 1)
            floors[c - 1].add(d - 1)

        floors[0].add(0)
        floors[n - 1].add(m - 1)

        dist = defaultdict(lambda: float('inf'))
        dist[(0,0)] = 0

        for i, floor in enumerate(floors):
            columns = sorted(list(floor))
            pq = []
            for col in columns:
                if dist[(i, col)] < float('inf'):
                    heappush(pq, (dist[(i, col)], col))
            while pq:
                room_dist, room_col = heappop(pq)
                idx = bisect_left(columns, room_col)

                if idx > 0:
                    n_dist = abs(columns[idx - 1] - columns[idx]) * x[i] + room_dist
                    if n_dist < dist[(i,columns[idx - 1])]:
                        dist[(i, columns[idx - 1])] = n_dist
                        pq.append((n_dist, columns[idx - 1]))

                if idx < len(columns) - 1:
                    n_dist = abs(columns[idx + 1] - columns[idx]) * x[i] + room_dist
                    if n_dist < dist[(i, columns[idx + 1])]:
                        dist[(i, columns[idx + 1])] = n_dist
                        pq.append((n_dist, columns[idx + 1]))

            for b, c, d, h in ladders[i]:
                dist[(c, d)] = min(dist[(c, d)], dist[(i,b)] - h)

        if dist[(n-1, m-1)] == float('inf'):
            print("NO ESCAPE")
        else:
            print(dist[(n-1, m-1)] )

main()
