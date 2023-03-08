# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root, max_ = float('inf'), min_ =  float('-inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
     
        
        
        
        if root is None:
            return True
        
        # print(root.val, min_, max_)
        
        if  root.left and root.right is None:
            if min_ < root.left.val < root.val:
                
                return self.isValidBST(root.left, min(max_, root.val), min_)
            else:
                return False
        
        elif root.left is None and root.right:
            if max_ > root.right.val > root.val:
                return self.isValidBST(root.right, max_,  max(min_, root.val))
            else:
                return False
                
        
        elif root.left is None and root.right is None:
            return min_ < root.val < max_
        else:
            
            
            
            if min_ < root.left.val < root.val and max_ > root.right.val > root.val:
                
                return self.isValidBST(root.left, min(max_, root.val), min_) and self.isValidBST(root.right, max_,  max(min_, root.val))
            
            else:
                
                return False
            
            
            