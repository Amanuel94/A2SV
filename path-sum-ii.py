# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        if root is None:
            return []

        aux_root = TreeNode(root.val)

        def makeAux(aux_root, root, prefix_sum):


            aux_root.val =  prefix_sum + root.val

            if root.left:
                aux_root.left = TreeNode()
                makeAux(aux_root.left, root.left, aux_root.val)
            if root.right:
                aux_root.right = TreeNode()
                makeAux(aux_root.right, root.right, aux_root.val)

        makeAux(aux_root, root, 0)
        ans = []
        def dfs(aux, cur, root):
            
            if root is None:
                return 
            # print(root.val, aux.val)
            cur.append(root.val)
            if aux.val == targetSum and root.left is None and root.right is None:
                ans.append(cur[:])

            
            dfs(aux.left, cur, root.left)
            dfs(aux.right, cur, root.right)
            cur.pop()

        dfs(aux_root, [], root)
        return ans