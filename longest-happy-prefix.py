class Solution:
    def longestPrefix(self, s: str) -> str:
        
        n = len(s)
        LSP = [0]*n

        i, j  = 0, 1
        while j < n:
            if s[i] == s[j]:
                LSP[j] = i+1
                i+=1
                j+=1
            elif i == 0:
                j+=1
            else:
                i = LSP[i-1]
        return s[:LSP[-1]]