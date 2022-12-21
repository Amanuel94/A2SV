class Solution(object):
    def mergeAlternately(self, word1, word2):
        word  = word1 + word2
        i, j = 0, len(word1)
        k = 0
        out = ""
        while i < len(word1) and j < len(word):
            if k % 2  == 0:
                out += word[i]
                i+=1
            else:
                out+= word[j]
                j+=1
            k+=1
        if j < len(word):
            out+=word[k:]
        elif i < len(word1):
            out+= word[i:len(word1)]

        return out
