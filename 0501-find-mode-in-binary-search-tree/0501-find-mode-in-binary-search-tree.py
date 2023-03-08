# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        freq =  defaultdict(int)
        freq = self.inOrder(root, freq)
        max_ = max(freq.values())
        return [i for i in freq.keys() if max_ == freq[i]]
        
        
    def inOrder(self, root, freq):
        
        if root is None:
            return freq
            
        freq[root.val]+=1
        freq = self.inOrder(root.left, freq)
        freq = self.inOrder(root.right, freq)
        
        return freq