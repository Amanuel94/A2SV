# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dp(root):
            if root is None:
                return 0
            left_left, right_left, right_right, left_right= 0,0,0,0
            if root.left in memo:
                left = memo[root.left]
            else:
                left = dp(root.left)
            if root.right in memo:
                right = memo[root.right]
            else:
                right = dp(root.right)
            if root.left and root.left.left in memo:
                left_left = memo[root.left.left]
            elif root.left:
                left_left = dp(root.left.left)
            if root.left and root.left.right in memo:
                left_right = memo[root.left.right]
            elif root.left:
                left_right = dp(root.left.right)
            if root.right and root.right.right in memo:
                right_right = memo[root.right.right]
            elif root.right:
                right_right = dp(root.right.right)
            if root.right and root.right.left in memo:
                right_left = memo[root.right.left]
            elif root.right:
                right_left = dp(root.right.left)
            memo[root] = max(left+right, left_left+left_right+right_left+right_right+root.val)

            return memo[root]
        return dp(root)