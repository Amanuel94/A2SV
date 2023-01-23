class Solution(object):
    def cmp(self, str1, str2):
        return (str1 + str2 < str2 + str1)
    
    def largestNumber(self, nums):
        res = [str(i) for i in nums]
        self.Sort(res)
        res.reverse()
        return ("").join(res) if ("").join(res)[0] != "0" else "0"
    
    def Sort(self, arr):
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]

            self.Sort(L)
            self.Sort(R)

            i = j = k = 0
            while i < len(L) and j < len(R):
                if self.cmp(L[i], R[j]):
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1