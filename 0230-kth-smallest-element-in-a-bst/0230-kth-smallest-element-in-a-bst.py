# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        ans = self.inOrder(root)
        return ans[k-1]
        
    def inOrder(self, root):
        
        ans = []
        
        if root:
            ans.extend(self.inOrder(root.left))
            ans.append(root.val)
            ans.extend(self.inOrder(root.right))
            
        return ans
            
        
        
        