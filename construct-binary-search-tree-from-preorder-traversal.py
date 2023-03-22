# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        dummy = TreeNode()
        root = TreeNode(preorder[0])
        dummy.left = root
        nodes  = [root]
        flag = False
        i = 1
        while i < len(preorder):
            node = TreeNode(preorder[i])   
            # print(nodes)
            while nodes and nodes[-1].val < preorder[i]:
                flag = True
                root = nodes.pop()
            nodes.append(node)
            if flag:
                root.right = node
                root = root.right
            else:
                root.left = node
                root = root.left
                
            flag = False
            i+=1
        return dummy.left
                
            
        
