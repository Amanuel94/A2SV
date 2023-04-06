from collections import defaultdict
class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)


    def AddEdge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        
    def Vertex(self, u):
        print(*self.adj_list[u])


n = int(input())
k = int(input())
graph = Graph()   
for _ in range(k):
    op = list(map(int, input().split()))

    if op[0] == 1:
        graph.AddEdge(op[1], op[2])
    else:
        graph.Vertex(op[1])
