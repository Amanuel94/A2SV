class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        if k == 0:
            left = 0
            right = 0
            res =  ans = 0
            while right < len(s):
                if s[right] == s[left]:
                    res+=1
                    right+=1
                else:
                    ans = max(ans, res)
                    res = 0
                    left+=1
            return max(res,ans)
                    

        left = 0
        ans = 0
        
        
        d = Counter(s[:k])
        
        right = k
        while right < len(s):
            ans = max(right -left, ans)
            most_freq =  max(d,key =  d.get)
            m = {i for i in d if d[i] == d[most_freq]} # most frequent elements
            t = 1 if s[right] in m else 0
            if right - left + 1 - (d[most_freq] + t)  <=k:
                if s[right] in d:
                    d[s[right]]+=1
                else:
                    d[s[right]] = 1
                right+=1
            else:
                
                d[s[left]]-=1
                left+=1
            ans = max(right - left, ans)
        return ans
            
           
    
            
            
    
        

            
            
            