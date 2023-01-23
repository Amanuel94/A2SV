class Solution(object):
    def pancakeSort(self, arr):
    
        n = len(arr) # size of array
        i = n - 1

        pan = []

        while i >= 0:
            j = 0
            max_ = arr[0]
            largest = 0
            while j <= i:
                if arr[j] > arr[largest]:
                    largest = j
                j+=1
            pan.append(largest+1)
            pan.append(i+1)
            
            arr = arr[i:largest:-1]+ arr[:largest+1] + arr[i+1:]
            
            i-=1
        return pan
            
                
    
        