class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False
        else:
            if arr[0] > arr[1]:
                return False
            
            i = 1
            while i < len(arr) and arr[i-1] < arr[i]:
                i+=1
            i-=1
            while i < len(arr)-1 and arr[i+1] < arr[i]:
                i+=1
            return i == len(arr)-1 and arr[-1] < arr[-2]
            
            
        