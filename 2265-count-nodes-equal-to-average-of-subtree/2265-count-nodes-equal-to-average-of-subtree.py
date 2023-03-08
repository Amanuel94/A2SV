# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        aux =  self.createAuxiliary(root)
        
        return self.traverseAndCheck(root, aux)
    
    
    def traverseAndCheck(self, root, aux):
        
        if root is None:
            return 0
        count = self.traverseAndCheck(root.left, aux.left) + self.traverseAndCheck(root.right, aux.right)
        if root.val == aux.val[0]/aux.val[1]:
            count+= 1 
            
        return count
        
        
        
    def createAuxiliary(self, root):
         
        
        if root is None:
            
            return TreeNode((0, 0))
        
        aux = TreeNode()
        
        aux.left = self.createAuxiliary(root.left)
        aux.right = self.createAuxiliary(root.right)
        
        aux.val = (aux.left.val[0] + aux.right.val[0] + root.val, aux.left.val[1] + aux.right.val[1] + 1)
        
        return aux
        
        
        
        
        