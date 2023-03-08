# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        levels = self.levels(root, 0, [])
        return [level[-1] for level in levels ]        
        
    def levels(self, root, k, ans):
        
        if root is None:
            return ans
        
        if k < len(ans):
            ans[k].append(root.val)
            
        else:
            ans.append([root.val])
            
        ans = self.levels(root.left, k+1, ans)
        ans = self.levels(root.right, k+1, ans)
        
        return ans