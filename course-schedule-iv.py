class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        A = [[inf]*numCourses for _ in range(numCourses)]
        for pre, course in  prerequisites:
            A[pre][course] =1
        for i in range(numCourses):
            A[i][i] = 0
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    A[i][j] = min(A[i][j], A[i][k] + A[k][j])
        answer = []
        for p, c in queries:
            # print(A)
            answer.append(A[p][c] <  inf)
        return answer