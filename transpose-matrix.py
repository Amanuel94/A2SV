class Solution(object):
    def transpose(self, matrix):
        tr = [[0]*len(matrix) for i in range(len(matrix[0]))]
        for i, row in enumerate(matrix):
            for j in range(len(tr)):
                tr[j][i] = row[j]
        return tr
