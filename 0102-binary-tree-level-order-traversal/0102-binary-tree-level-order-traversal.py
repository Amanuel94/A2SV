# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        return self.k_level(root, 0, [])
        
        
        
    def k_level(self, root, k, ans):
        
        if root is None:
            return ans
        
        
        
        if k < len(ans):
            ans[k].append(root.val)
        else:
            ans.append([root.val])
        
        ans = self.k_level(root.left, k+1, ans)
        ans = self.k_level(root.right, k+1, ans)
        
        return ans
        
        
        
        