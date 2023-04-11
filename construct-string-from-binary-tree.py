# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        return self.preOrder(root)


    def preOrder(self, root):
        if root is None:
            return ""
        ans = str(root.val)

        left = self.preOrder(root.left)
        right = self.preOrder(root.right)

        if left or not left and right:
            ans = ans + "(" + left + ")"
        if right:
            ans = ans + "(" + right + ")"

        return ans