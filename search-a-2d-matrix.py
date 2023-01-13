class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """


        n_rows = len(matrix)
        n_cols = len(matrix[0])

        if n_rows*n_cols == 1 and matrix[0][0] == target:
            return True
        elif n_rows*n_cols == 1 and matrix[0][0] != target:
            return False
        else:

            flattened_length = n_rows*n_cols
            l = 0
            r = flattened_length-1
            found = False

            while not found and l < r:
                mid = (l + r)/2
                if matrix[mid//n_cols][mid%n_cols] == target or matrix[l//n_cols][l%n_cols] ==target or  matrix[r//n_cols][r%n_cols] == target:
                    return True
                else:
                    if matrix[mid//n_cols][mid%n_cols] < target:
                        l = mid+1
                    else:
                        r = mid-1
                
            return False
