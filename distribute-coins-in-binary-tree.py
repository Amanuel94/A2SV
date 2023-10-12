# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:

        ans = 0
        def dfs(node, parent):
            nonlocal ans
            if node is None:
                return 
        
            dfs(node.left, node)
            dfs(node.right, node)

            if parent:
                if node.val > 1:
                    parent.val+=(node.val-1)
                    ans+=(node.val-1)
                else:
                    parent.val = parent.val+ node.val - 1
                    ans+=abs(1- node.val)
                node.val = 1

        dfs(root, None)
        return ans