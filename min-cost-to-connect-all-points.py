class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        def distance(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return abs(x1-x2)+abs(y1-y2)

        # sort all possible edges
        edges = []
        for i, pointi in enumerate(points):
            for j, pointj in enumerate(points):
                if i != j:
                    edges.append([distance(pointi, pointj), i, j])
        edges.sort()
        
        # connect edeges
        group = {i:i for i in range(n)}
        def getGroup(i):
            if i == group[i]:
                return i
            group[i] = getGroup(group[i])
            return group[i]

        total_cost = 0
        number_of_added_edges = 0

        for cost, i, j in edges:
            if getGroup(i)!=getGroup(j):
                group[getGroup(i)] = getGroup(j)
                total_cost+=cost
                number_of_added_edges+=1
            if number_of_added_edges == n-1:
                break
        return total_cost