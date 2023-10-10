class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        lim = len(b)//len(a) + 2
        n_copies = 0
        LSP = [0]*len(b)

        i, j = 0, 1
        while j < len(b):

            if b[i] == b[j]:
                LSP[j] = i+1
                i+=1
                j+=1
            elif i == 0:
                j+=1
            else:
                i = LSP[i-1]
        i, j = 0, 0
        while n_copies < lim:
            n_copies+=1
            i = 0
            while i < len(a):
                if a[i] == b[j]:
                    i+=1
                    j+=1
                elif j == 0:
                    i+=1
                else:
                    j = LSP[j-1]

                if j == len(b):
                    return n_copies
        return -1