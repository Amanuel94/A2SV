class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:


        tower = [[0]*i for i in range(1,101)]

        # print(tower)
        tower[0][0] = poured
        for i in range(99):
            for j in range(i+1):
                flow = max((tower[i][j]-1)/2, 0)
                tower[i+1][j] +=  flow
                tower[i+1][j+1] += flow

                tower[i][j] = min(1, tower[i][j])
        return tower[query_row][query_glass]