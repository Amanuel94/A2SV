# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pre = []
        def preOrder(root):
            if root is None:
                return
            
            preOrder(root.left)
            pre.append(root.val)
            preOrder(root.right)

        preOrder(root)
        if len(set(pre)) == len(pre) and pre == sorted(pre) :
            return True
        return False