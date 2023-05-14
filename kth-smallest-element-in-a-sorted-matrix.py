class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap =  [float('-inf')]*k
        for row in matrix:
            for col in row:
                heappushpop(heap, -col)
        # print(heap)
        return -heappop(heap)