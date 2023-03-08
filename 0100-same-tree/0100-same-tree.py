# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        if p is None and q is None:
            
            return True
        elif p and q is None:
            
            return False
        
        elif q and p is None:
            return False
        
        else:
            
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)