# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


class TreeNode:

    def __init__(self, val = None):

        self.val = val
        self.children = []

    def isInteger(self):
        return self.val != None



class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
        self.root = TreeNode()
        self.res =  []
    
        for ele in nestedList:
            # self.root.children.append(self.makeTree(ele))
            self.makeTree(ele)

        # self.preOrder(self.root)
        self.index = 0
        
    
    def next(self, nestedList = None) -> int:
        self.index+=1
        return self.res[self.index-1]


    def preOrder(self, root):
        
        if root.val is not None:
            self.res.append(root.val)
        for ele in self.root.children:
            self.preOrder(ele)

        
    
    def hasNext(self) -> bool:
        
        return self.index < len(self.res)

    
    def makeTree(self, nestedInt):
        # print(nestedInt.getInteger())
        if nestedInt.getInteger() is not None:
            self.res.append(nestedInt.getInteger())
        # root = TreeNode(nestedInt.getInteger())
        for ele in nestedInt.getList():
            # root.children.append(self.makeTree(ele))
            self.makeTree(ele)
        # return root


         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())