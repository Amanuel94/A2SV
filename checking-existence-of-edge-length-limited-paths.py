class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:

        """
        construct the thing from bottom up
        """
        edgeList.sort(key = lambda x:x[2])
        indices = list(range(len(queries)))
        indices.sort(key = lambda x:queries[x][2]) # iterate thorugh the queries, smallest limits first

        component = {i:i for i in range(n)}
        def getComponent(i):
            if i == component[i]:
                return i
            component[i] = getComponent(component[i])
            return component[i]

        def connect(ui, vi):
            component[getComponent(ui)] = getComponent(vi)

        def areConnected(a, b):
            return getComponent(a) == getComponent(b)

        answer = [0]*len(queries)
        cur_edge = 0
        for index in indices:
            p, q, limit = queries[index]
            while cur_edge < len(edgeList):
                u, v, dist = edgeList[cur_edge]
                
                if dist < limit:
                    connect(u, v)
                    cur_edge+=1
                else:
                    break

            answer[index] = areConnected(p,q)
        return answer