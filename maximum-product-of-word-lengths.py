class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        alpha = []
        for word in words:
            n = 0
            for c in word:
                n|= 1<<(ord(c)-97)
                
            alpha.append(n)
            
        i= max_ =0
        # print(list(map(bin, alpha)))
        while i < len(words)-1:
            j = i+1
            while j < len(words):
                
                if alpha[i]&alpha[j] == 0:
                    max_ = max(max_, len(words[i])*len(words[j]))
                j+=1
            i+=1
            
        return max_
