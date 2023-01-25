class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        if word1 == "":
            return word2
        if word2 == "":
            return word1
        
        
        w1 = list(word1)
        w2 = list(word2)
        
        if len(w1) < len(w2):
            w1.extend(['0']*(len(w2)-len(w1)))
        if len(w2) < len(w1):
            w2.extend(['0']*(len(w1)-len(w2)))
        
        n1 = len(w1)
        n2 = len(w2)
        
        p1 = 0
        p2 = 0
        
        ans = ""
        
        while p1 < n1 and  p2 < n2:
            if w1[p1:] < w2[p2:]:
                w1, w2 = w2, w1
                p1, p2 = p2, p1
                
            if w1[p1] < w2[p2]:
                ans+=w2[p2]
                p2+=1
            else:
                ans+=w1[p1]
                p1+=1
        while p1 < len(w1):
            ans+=w1[p1]
            p1+=1
        while p2 < len(w2):
            ans+=w2[p2]
            p2+=1
            
        return ans[:ans.index('0')] if len(word1) != len(word2) else ans
        
            
        