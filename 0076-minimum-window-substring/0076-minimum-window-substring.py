class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        p = Counter(t)
        
        l  = 0
        st = defaultdict(int)
        
        flag = False
        
        ans_l = ans_r = 0
        
        min_l = float('inf')
        
        for r in range(len(s)):
            st[s[r]]+=1
            
            
            while self.checkSubString(p, st):
                flag = True
                if min_l > r - l + 1:
                    min_l = r - l +1
                    ans_l = l
                    ans_r = r
                st[s[l]]-=1
                l+=1            
                
        return s[ans_l:ans_r+1] if flag else ""
        
        
        
        
    def checkSubString(self, t, s):
        
        for key in t:
            if s.get(key, 0) - t[key] < 0:
                return False
        return True
        
        
        