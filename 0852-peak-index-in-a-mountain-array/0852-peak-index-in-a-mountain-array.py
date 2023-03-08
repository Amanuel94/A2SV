class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        low = 1
        high = len(arr)-2
        
        while low < high:
            
            mid =  (low+ high)//2
            
            if self.isPeak(arr, mid) == 0:
                
                return mid
            elif self.isPeak(arr, mid) == -1:
                
                low = mid+1
            else:
                high = mid-1
                
        return low
            
            
            
    def isPeak(self, arr, i):
            
        if arr[i-1] < arr[i] > arr[i+1]:
            return 0
        elif arr[i-1] < arr[i] < arr[i+1]:
            return -1
        else:
            return 1
                