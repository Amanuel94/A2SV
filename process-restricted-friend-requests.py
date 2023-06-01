class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:


        """
        iterate every time through restrictions to check if each friend request is 
        valid or successful
        """

        group = {i:i for i in range(n)}
        def getGroup(i):
            if i == group[i]:
                return i
            group[i] = getGroup(group[i])
            return group[i]

        result = []
        for request in requests:
            ui, vi = request # request to be checked
            isSuccessful = True
            i = 0
            while isSuccessful and i < len(restrictions):
                ai, bi = restrictions[i]
                
                if {getGroup(ai), getGroup(bi)} == {getGroup(ui), getGroup(vi)}:
                    isSuccessful = False
        
                i+=1
            result.append(isSuccessful)
            if isSuccessful:
                group[getGroup(ui)] = getGroup(vi)

        return result