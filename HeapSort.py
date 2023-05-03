class Solution:
    def heapifyDown(self, arr, n, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapifyDown(arr, n, largest)
    
    def buildHeap(self,arr,n):
        for num in range(n//2 - 1, -1, -1):
            self.heapifyDown(arr, n, num)

    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        
        for i in range(n-1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapifyDown(arr, i, 0)
        
        
