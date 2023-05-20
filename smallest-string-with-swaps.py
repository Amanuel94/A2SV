class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        A = {}
        B = {}
        p = {i:i for i in range(len(pairs))}

        def getP(i):
            if i == p[i]:
                return i
            p[i] = getP(p[i])
            return p[i]
        for i, pair in enumerate(pairs):
            a,b = pair
            if a in A:
                p[getP(i)]= getP(A[a])
            else:
                A[a] = i
            if b in A:
                p[getP(i)] = getP(A[b])
            else:
                A[b] = i
        print(p)
        groups = defaultdict(set)
        for i in range(len(pairs)):
            groups[getP(i)].add(pairs[i][0])
            groups[getP(i)].add(pairs[i][1])
        # print(groups)
        ans = list(s)
        for i in groups:
            li = sorted(list(groups[i]), key = lambda x:s[x])
            sli = sorted(list(groups[i]))
            print(i, li)
            n = len(li)
            for j, i in enumerate(li):
                ans[sli[j]] = s[i]
        return "".join(ans)