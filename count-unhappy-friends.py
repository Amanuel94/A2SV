class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:

        preferences = [{friend: index for index, friend in enumerate(pref)} for pref in preferences]


        def f(x, y, u, v):
            return preferences[x][u] < preferences[x][y]  and  (preferences[u][x]  < preferences[u][v]) 
        
        count = 0
        unhappy = set()
        n_pairs = len(pairs)
        for i in range(n_pairs):
            x, y = pairs[i]
            for j in range(i+1, n_pairs):
                u, v = pairs[j]
                if i != j:
                    if f(x, y, u, v):
                        unhappy.add(x)
                        unhappy.add(u)
                    if f(y,x,u,v):
                        unhappy.add(y)
                        unhappy.add(u)
                    if f(x,y,v,u):
                        unhappy.add(x)
                        unhappy.add(v)
                    if f(y,x,v,u):
                        unhappy.add(y)
                        unhappy.add(v)
                    # break
        return len(unhappy)