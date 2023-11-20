# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        ans = []
        to_delete = set(to_delete)
        if root.val not in to_delete:
            ans.append(root)
        def dfs(node, par, side):
            
            if node is None:
                return
            # print(node.val)
            dfs(node.left, node, 0)
            dfs(node.right, node, 1)

            if node.val in to_delete:
                ans.append(node.left)
                ans.append(node.right)
                if par:
                    if side:
                        par.right = None
                    else:
                        par.left = None
            
        dfs(root,None, 0)

        return [root for root in ans if root]
            

            
            
        