class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, node: int) -> int:

        A = [[inf]*n for _ in range(n)]
        for u, v, w in times:
            A[u-1][v-1] = w

        for i in range(n):
            A[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                        A[i][j] = min(A[i][j], A[i][k]+A[k][j])
        ans = 0
        for i in range(n):
            ans = max(ans, A[node-1][i])
        return ans if ans < inf else -1