class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        incs = ["0001", "0010", "0100", "1000"]
        vis = set(["0000"])
        que = deque(["0000"])
        count = -1
        def plus(b, a, op):
            a, b  = str(a), str(b)
            ans = ""
            i = len(a)-1
            j = len(b)-1


            while i >= 0 and j >= 0:
                cur = int(a[i]) + int(b[j]) if op == '+' else int(a[i]) - int(b[j])
                if cur == 10:
                    cur = "0"
                elif cur == -1:
                    cur = "9"
                else:
                    cur = str(cur)
                ans =  cur + ans
                i-=1
                j-=1
                
            return ans


        while que:
            len_ = len(que)
            count+=1
            # print(que)
            for _ in range(len_):
                cur = que.popleft()
                if cur == target:
                    return count
                
                for inc in incs:
                    if plus(inc, cur, '+') not in deadends and plus(inc, cur, '+') not in vis:
                        vis.add(plus(inc, cur, '+'))
                        que.append(plus(inc, cur, '+')) 
                    if plus(inc, cur, '-') not in deadends and plus(inc, cur, '-') not in vis:
                        vis.add(plus(inc, cur, '-'))
                        que.append(plus(inc, cur, '-'))
        return -1