#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here
        
        j =  i + 1
        temp = arr[i]
        s = i
        while j < len(arr):
            if arr[j] < temp:
                temp, s = arr[j], j
            j+=1
        return s
        
        
    
    def selectionSort(self, arr,n):
        #code here
        i = 0
        while i < n-1:
            j = self.select(arr, i)
            arr[i], arr[j] = arr[j], arr[i]
            
            i+=1
        return 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends