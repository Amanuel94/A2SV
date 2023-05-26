class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:

        """
        maintain order from the right
        """

        n = len(arr)
        i = n - 1

        while i > 0 and arr[i] >= arr[i-1]: # until reach local minimum
            i-=1
           
        if i > 0:
            if arr[i-1] > arr[n-1]:
                arr[i-1], arr[n-1] = arr[n-1], arr[i-1]
            else:
                t = s = i
                while t < n:
                    if arr[s] < arr[t] < arr[i-1]:
                        s = t
                    t+=1
                arr[i-1], arr[s] = arr[s], arr[i-1]

        return arr