# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        
        
        d =  defaultdict(int)
        
        return self.updateTree(root, d, 0, targetSum)
        
        
    def updateTree(self, root, d, ans, targetSum):
        
        if root is None:
            return ans
        
        if root.left:
            root.left.val+=root.val
            
            
        if root.right:
            root.right.val+=root.val
            
        ans+=d[root.val - targetSum]
        
        if root.val == targetSum:
            ans+=1
        
        d[root.val]+=1
        ans = self.updateTree(root.left, d, ans, targetSum)
        ans = self.updateTree(root.right, d, ans, targetSum)
        d[root.val]-=1
        
        return ans