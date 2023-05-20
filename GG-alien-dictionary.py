#User function Template for python3
from collections import defaultdict, deque
class Solution:
    def __init__(self):
        self.inc = defaultdict(int)
        self.alphabet = set()
    def createGraph(self, alien_dict):
        graph = defaultdict(list)
        pointer_stack = []
        i = 0
        while i < len(alien_dict)-1:
            j = 0
            while j < min(len(alien_dict[i]), len(alien_dict[i+1])) and alien_dict[i][j] == alien_dict[i+1][j]:
                j+=1
            if j < min(len(alien_dict[i]), len(alien_dict[i+1])):
                graph[alien_dict[i][j]].append(alien_dict[i+1][j])
                self.inc[alien_dict[i+1][j]]+=1
                # if self.inc['d'] == 2:
                #     print(alien_dict[i])
            self.alphabet = self.alphabet | set(alien_dict[i])
            i+=1
        self.alphabet = self.alphabet | set(alien_dict[i])
        return graph
  
    
    def findOrder(self,alien_dict, N, K):
        # code here
        graph =  self.createGraph(alien_dict)
        # print(self.alphabet)
        # print(self.inc)
        q = deque([i for i in self.alphabet if self.inc[i] == 0])
        # print(q)
        # print(dict(graph))
        order = []
        while q:
            x = q.popleft()
            order.append(x)
            for nbr in graph[x]:
                self.inc[nbr]-=1
                if self.inc[nbr] == 0:
                    q.append(nbr)
        
        # print(order)
        return order
    


