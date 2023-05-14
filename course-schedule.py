class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph =  defaultdict(list)
        inc = [0]*numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            inc[course]+=1
        
        q = deque([i for i in range(numCourses) if inc[i] == 0])
        # print(q)
        order = []
        while q:
            x = q.popleft()
            order.append(x)
            for nbr in graph[x]:
                # if inc[nbr] > 0:
                    inc[nbr]-=1
                    if inc[nbr]==0:
                        q.append(nbr)
                    # elif inc[nbr] < 0:
                    #     return False

        
        return sum(inc) == 0