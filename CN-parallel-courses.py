from collections import defaultdict, deque
def parallelCourses(n, prerequisites):

    
    # T = int(input())
    # for _ in range(T):
        N = n
        M = len(prerequisites)
        graph = defaultdict(list)
        inc = [0]*N

        for __ in range(M):
            A, B = prerequisites[__]
            graph[A].append(B)
            inc[B-1]+=1
        q = deque([i+1 for i in range(N) if inc[i]==0])
        count = 0
        while q: 
            tog = len(q)
            count+=1
            for _ in range(tog):
                x =  q.popleft()
                for nbr in graph[x]:
                    inc[nbr-1]-=1
                    if inc[nbr-1] == 0:
                        q.append(nbr)
        if sum(inc):
            return -1
        return count           
