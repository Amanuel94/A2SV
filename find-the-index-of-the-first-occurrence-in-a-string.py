class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        n = len(needle)
        LSP = [0]*len(needle)

        i, j =  0, 1
        while j < n:
            if needle[i] == needle[j]:
                LSP[j] = i + 1
                i+=1
                j+=1
            else:
                if i != 0:
                    i = LSP[i-1]
                else:
                    j+=1
        
        i, j =  0, 0
        while j < len(haystack):
            if needle[i] == haystack[j]:
                i+=1
                j+=1
            else:
                if i != 0:
                    i = LSP[i-1]
                else:
                    j+=1
            if i == n:
                return j - n
        return -1