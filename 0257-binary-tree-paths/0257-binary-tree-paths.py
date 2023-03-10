# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    
        
        return self.backtrack(root)
        
        
        
    def backtrack(self, root):
        
        if root.left is None and root.right is None:
            return [str(root.val)]
        
        elif root.left is None:
            res = self.backtrack(root.right)
        
            i = 0
            while i < len(res):

                res[i] = str(root.val) + "->"+ res[i]    
                i+=1
                
        elif root.right is None:
            res = self.backtrack(root.left)
            i = 0
            while i < len(res):

                res[i] = str(root.val) + "->"+ res[i]    
                i+=1
            
        else:
            res = self.backtrack(root.left) + self.backtrack(root.right)
            i = 0
            while i < len(res):

                res[i] = str(root.val) + "->"+ res[i]    
                i+=1
            
        return res
            
            
            
            
        
        



        
        
        
        
        
            
            

        