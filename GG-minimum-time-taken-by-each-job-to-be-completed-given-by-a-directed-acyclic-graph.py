from typing import List


from typing import List
from collections import defaultdict, deque


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        inc = [0]*n
        graph = defaultdict(int)
        for u, v in edges:
            graph[u]|= (1<<(v-1))
            inc[v-1]+=1
        q = deque([i+1 for i in range(n) if inc[i] == 0])
        ans = [0]*n
        cur = 0
        while q:
            batch = len(q)
            cur+=1
            for _ in range(batch):
                x = q.popleft()
                ans[x-1] = cur
                nbrs = [i+1 for i in range(n) if graph[x]>>i & 1]
                for nbr in nbrs:
                    inc[nbr-1]-=1
                    if inc[nbr-1]== 0:
                        q.append(nbr)
        return ans
