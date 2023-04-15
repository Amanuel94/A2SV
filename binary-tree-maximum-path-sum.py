# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return float('-inf')

        max_ =float('-inf')
        def adder(root):
            nonlocal max_
            if root is None:
                return float('-inf')
            prefix = adder(root.left)
            suffix = adder(root.right)

            max_ = max(prefix+root.val,suffix+root.val, prefix+suffix+root.val, max_ , root.val)
            return max(prefix+root.val, suffix+root.val, 0, root.val)

        adder(root)
            
        return max_