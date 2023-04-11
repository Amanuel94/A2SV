# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        paths = []
        def dfs(root, cur):
            nonlocal paths
            ans = ""
            if root.left is None and root.right is None:
                paths.append(cur + str(root.val))
                return

            cur = cur + str(root.val)
            if root.left is not None:
                dfs(root.left, cur)
            if root.right is not None:
                dfs(root.right, cur)

        dfs(root, "")
        ans = 0
        for path in paths:
            ans+=int(path)

        return ans