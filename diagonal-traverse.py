class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        pivots = {}
        for i in range(len(mat)):
            for j in range(len(mat[i])):

                if i + j not in pivots:

                    pivots[i+j] = [mat[i][j]]
                else:

                    pivots[j+i].append(mat[i][j])
        res = []

        for entry in pivots.keys():
			
            if entry % 2 == 0:

                [res.append(x) for x in pivots[entry][::-1]]
            else:

                [res.append(x) for x in pivots[entry]]

        return res
                				
Console
