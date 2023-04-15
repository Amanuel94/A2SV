class TreeNode:
    def __init__ (self, val = "king", children = []):
        self.val = val
        self.children = children[:]
        self.isDead = False

class ThroneInheritance:
    def __init__(self, kingName: str):

        self.king = TreeNode(kingName)
        self.dict = {kingName:self.king}

    def birth(self, parentName: str, childName: str) -> None:
        new_born = TreeNode(childName)
        # par = self.getNode(parentName)
        par  = self.dict[parentName]
        self.dict[childName] = new_born
        par.children.append(new_born)
    
        

    def death(self, name: str) -> None:
        dead = self.dict[name]
        dead.isDead = True

    def getInheritanceOrder(self) -> List[str]:
        ans = []
        def preOrder(root):
            nonlocal ans
            if root is None:
                return
            if not root.isDead:
                ans.append(root.val)
            for child in root.children:
                preOrder(child)
        preOrder(self.king)
        return  ans
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()