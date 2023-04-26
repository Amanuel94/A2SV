class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.tree = defaultdict(list)
        self.locked_by = defaultdict(int)

        for u, v in enumerate(parent):
            if v != -1:
                self.tree[v].append(u)
        

    def lock(self, num: int, user: int) -> bool:
        
        if self.locked_by[num]:
            # print(self.locked_by)
            return False
        self.locked_by[num] = user
        # print(self.locked_by)
        return True
        

    def unlock(self, num: int, user: int) -> bool:
        if self.locked_by[num] == user:
            self.locked_by[num] = 0
            # print(self.locked_by)
            return True
        # print(self.locked_by)
        return False


    def isUpgradable(self, num):
        par = num
        while par !=-1:
            if self.locked_by[par]:
                return False
            par = self.parent[par]
        def dfs(num):
            ans = False
            for nbr in self.tree[num]:
                if self.locked_by[nbr] != 0:
                    return True
                ans = ans or dfs(nbr)
            return ans
        return dfs(num)
    def upgrade(self, num: int, user: int) -> bool:
        if self.isUpgradable(num):
            def unlockAll(num):
                self.locked_by[num] = 0
                for nbr in self.tree[num]:
                    unlockAll(nbr)
            unlockAll(num)
            self.locked_by[num] = user
            # print(self.locked_by)
            return True
        # print(self.locked_by)
        return False


        
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)