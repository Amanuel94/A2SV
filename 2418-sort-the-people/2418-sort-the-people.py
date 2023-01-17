class Solution(object):
    def sortPeople(self, names, h):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        
        i = len(h)-1
        while i >= 0:
            j = 0
            while j < i:
                if h[j] < h[j+1]:
                    h[j], h[j+1] = h[j+1], h[j]
                    names[j], names[j+1] = names[j+1], names[j]
                j+=1
            i-=1
        return names
            
        