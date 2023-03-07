# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root, max_ = 0):
        """
        :type root: TreeNode
        :rtype: int
        """ 
        
        if root ==  None:
            return 0
        
        
        return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1 )
        