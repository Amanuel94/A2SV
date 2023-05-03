# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def traverse(root):
            if root.right is None and root.left is None:
                return
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                traverse(root.left)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                traverse(root.right)
                
        traverse(root)
        q = deque([target.val])
        vis = set([target.val])
        count = -1
        while q:
            lvl = len(q)
            count+=1
            if count == k:
                return list(q)
            for _ in range(lvl):
                node = q.popleft()
                for nbr in graph[node]:
                    if nbr not in vis:
                        q.append(nbr)
                        vis.add(nbr)
        return []