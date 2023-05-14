class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rows = defaultdict(int)
        cols = defaultdict(int)

        graph_rows = defaultdict(list)
        graph_cols = defaultdict(list)
        inc = [0]*k

        for above, below in rowConditions:
            graph_rows[above].append(below)
            inc[below-1]+=1
        q = deque([i+1 for i in range(k) if inc[i]== 0])
        row = -1
        while q:
    
            cell = q.popleft()
            row+=1
            rows[cell] = row
            for nbr in graph_rows[cell]:
                inc[nbr-1]-=1
                if inc[nbr-1]==0:
                    q.append(nbr)
        if sum(inc):
            return []

        inc = [0]*k
        for left, right in colConditions:
            graph_cols[left].append(right)
            inc[right-1]+=1
        
        # print(graph_cols, inc)
        q = deque([i+1 for i in range(k) if inc[i] == 0])
        col = -1
        while q:
            cell = q.popleft()
            col+=1
            cols[cell] = col
            for nbr in graph_cols[cell]:
                inc[nbr-1]-=1
                if inc[nbr-1]==0:
                    q.append(nbr)
        print(inc)
        if sum(inc):
            return []
        matrix = [[0]*k for _ in range(k)]
        for i in range(k):
            matrix[rows[i+1]][cols[i+1]] = i+1
        return matrix