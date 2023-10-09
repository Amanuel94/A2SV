# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        counter = defaultdict(int)
        ans = []
        def inOrder(root):
            if root is None:
                return ""
            
            left = inOrder(root.left)
            right = inOrder(root.right)

            id = f"({left}){root.val}({right})"
            counter[id]+=1
            if counter[id] == 2:
                ans.append(root)
            return id
        inOrder(root)
        return ans