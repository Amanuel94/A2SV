# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode], ans = None) -> List[int]:
        
        if root == None:
            return ans
        
        if not ans:
            ans = []
        
        ans = self.inorderTraversal(root.left, ans)
        
        ans.append(root.val)
        
        ans = self.inorderTraversal(root.right, ans)
        
        return ans
    
    
        