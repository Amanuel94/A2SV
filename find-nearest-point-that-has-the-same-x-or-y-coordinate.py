class Solution(object):
    def nearestValidPoint(self, x, y, points):
        min_dist = float('inf')
        min_i = 0

        for i, point in enumerate(points):

            if point[0] == x or point[1] == y:

                if min_dist > abs(point[0] - x) + abs(point[1] - y):
                    min_dist =  abs(point[0] - x) + abs(point[1] - y)
                    min_i = i

        return min_i if (min_dist != float('inf')) else -1
