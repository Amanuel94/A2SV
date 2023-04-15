class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree =  defaultdict(list)
        for i, rel in enumerate(parent):
            if rel != -1:
                tree[(i, s[i])].append((rel, s[rel]))
                tree[((rel, s[rel]))].append((i, s[i]))
            else:
                root = (i, s[i])

        max_ = 1
        def pathMaker(tree, node, vis):
            nonlocal max_
            vis.add(node)
           
            path1, path2 = 0, 0
            for nbr in tree[node]:
                if nbr not in vis:
                    path = pathMaker(tree, nbr, vis)
                    if nbr[1] == node[1]:
                        path = 0

                    if path >= path1:
                        path2 =  path1
                        path1 = path
                    elif path > path2:
                        path2 = path

            max_ = max(max_, path1 + path2 + 1)
            return max(path1, path2) + 1

        pathMaker(tree, root, set())
        return max_