class Solution(object):
    def sortPeople(self, names, h):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        # bubble sort
        i = len(h)-1
        swapped = False
        while i >= 0:
            j = 0
            while j < i:
                if h[j] < h[j+1]:
                    swapped = True
                    h[j], h[j+1] = h[j+1], h[j]
                    names[j], names[j+1] = names[j+1], names[j]
                j+=1
            if not swapped:
                return names
            i-=1
        return names
        
        
        
        # i = 0
        # while i < len(h)-1:
        #     j = i+1
        #     large = j
        #     while j < len(h):
        #         if h[large] < h[j]:
        #             large = j
        #         j+=1
        #     h[i], h[large] = h[large], h[i]
        #     names[i], names[large] = names[large], names[i]
        #     i+=1
        # return names
        