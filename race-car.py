class Solution:
    def racecar(self, target: int) -> int:
        init = (0,1)
        vis = set([init])
        que = deque([init])

        count = -1
        while que:
            level = len(que)
            count+=1
            for _ in range(level):
                p, s = que.popleft()
                if p == target:
                    return count
                if (p, -s//abs(s)) not in vis:
                    que.append((p,-s//abs(s)))
                    vis.add((p,-s//abs(s)))
                if (p+s, 2*s) not in vis:
                    que.append((p+s, 2*s))
                    vis.add((p+s, 2*s))
        return count