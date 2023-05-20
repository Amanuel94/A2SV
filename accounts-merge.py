class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = defaultdict(str)
        def getP(i):
            if parent[i] == i or parent[i] == "":
                return i
            parent[i] = getP(parent[i])
            return parent[i]

        for i, account in enumerate(accounts):
            u_name, *emails =  account

            parent[getP(emails[0])] = str(i)
            j = 1
            while j < len(emails):
                parent[getP(emails[j])] =  getP(emails[j-1])
                j+=1
        ans = []
        res = defaultdict(list)
        s = list(parent.keys())[:]
        for account in s:
            if '@' in account:
                p = getP(account)
                res[int(p)].append(account)
        for j in res:
            ans.append([accounts[j][0]] + sorted(res[j]))
        return ans