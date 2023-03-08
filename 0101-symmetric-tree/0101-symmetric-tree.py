# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        p = root.left
        q = root.right
        
        return self.isSameTree(p, q)
        
        
    def isSameTree(self, p, q):
        
        
        
        if p is None and q is None:
            
            return True
        elif p and q is None:
            
            return False
        
        elif q and p is None:
            return False
        
        else:
            
            
            return p.val == q.val and self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)
        
            
        
        
        
        
            
        
        
        
        