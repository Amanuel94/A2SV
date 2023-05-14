class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        graph = defaultdict(list)
        inc = defaultdict(int)

        for i, ings in enumerate(ingredients):
            for j, ing in enumerate(ings):
                graph[ing].append(recipes[i])
                if ing not in inc:
                    inc[ing] = 0
                inc[recipes[i]]+=1
        # print(inc)
        q = deque(supplies)
        ans = []
        while q:
            x = q.popleft()
            for nbr in graph[x]:
                if inc[nbr] > 0:
                    inc[nbr]-=1
                    if inc[nbr] == 0:
                        if nbr in recipes:
                            ans.append(nbr)
                        q.append(nbr)
                    
                

        return ans