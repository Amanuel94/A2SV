# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        pos = []

        def dfs(node, val, lvl):
            if node is None:
                return

            if len(pos)-1 < lvl:
                pos.append([val])
            else:
                pos[lvl].append(val)
            
            dfs(node.left, 2*val, lvl+1)
            dfs(node.right, 2*val+1, lvl+1)
        dfs(root, 0, 0)
        # print(pos)
        return max([max(lvl) - min(lvl)+1 for lvl in pos])