"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        ans = 0
        def dfs(root, depth):

            nonlocal ans
            if root is None:
                ans =  max(ans, depth)
                return
            elif root.children == []:
                ans =  max(ans, depth+1)
                return

            for node in root.children:
                dfs(node, depth+1)

        dfs(root, 0)
        return ans