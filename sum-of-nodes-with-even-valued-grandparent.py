# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        nodes = []

        # def grandchildren(root):
        #     ans = []
        #     if root:
        #         if root.left:
        #             if root.left.left:
        #                 ans.append(root.left.left.val)
        #             if root.left.right:
        #                 ans.append(root.right)

        root.val = (root.val, False)

        def dfs(root):
            nonlocal nodes
            if root is None:
                return
            if root.val[0]%2 == 0:
                if root.left:
                    root.left.val = (root.left.val, True)
                if root.right:
                    root.right.val = (root.right.val, True)
            else:
                if root.left:
                    root.left.val = (root.left.val, False)
                if root.right:
                    root.right.val = (root.right.val, False)

            if root.val[1]:
                if root.left:
                    nodes.append(root.left.val[0])
                if root.right:
                    nodes.append(root.right.val[0])

            dfs(root.left)
            dfs(root.right)


        dfs(root)
        return sum(nodes)