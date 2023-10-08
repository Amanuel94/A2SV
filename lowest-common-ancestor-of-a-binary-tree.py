# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        LCA = root
        p_found, q_found = False, False

        def dfs(par, root):
            nonlocal LCA, p_found, q_found

            if root is None or (p_found and q_found):
                return

            if not p_found and not q_found:
                LCA = root

            p_found = p_found or (root.val == p.val)
            q_found = q_found or (root.val == q.val)
            
            dfs(LCA, root.left)
            dfs(LCA, root.right)
    
            if not p_found or not q_found:
                LCA = par
            
        dfs(root, root)
        return LCA