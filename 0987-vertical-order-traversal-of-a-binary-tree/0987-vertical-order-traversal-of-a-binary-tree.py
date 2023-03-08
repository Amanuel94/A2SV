# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        col_dict =  defaultdict(list)
        col_dict = self.columns(root, 0, 0, col_dict)
        
        col_dict = sorted(col_dict.items())
        
        ans = []
                
        for tup in col_dict:
            col = []
            tup[1].sort()
            for t in tup[1]:
                col.append(t[1])
                
            ans.append(col)
            
        return ans
                
        
        # return [i[1] for i in col_dict]
        
        
        
    def columns(self, root, row, col, col_dict):
        if root is None:
            return col_dict
        
        col_dict[col].append([row,root.val])
        
        col_dict =  self.columns(root.left, row + 1, col-1, col_dict)
        col_dict = self.columns(root.right, row+1, col+1, col_dict)
        
        return col_dict
        
        