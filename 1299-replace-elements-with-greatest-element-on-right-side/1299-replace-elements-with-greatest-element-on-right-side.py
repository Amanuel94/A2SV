class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        i = len(arr)-1
        maxima = arr[-1]
        while i > 0:
            temp = arr[i-1]
            arr[i-1]  = maxima
            maxima = max(maxima, temp)
            i-=1
        arr[-1] =-1
        return arr
    