class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        quar = len(s)//4
        
        excess = {i: Counter(s).get(i, 0) - quar for i in ['Q', 'W', 'E', 'R'] }
        
        if excess.values() == [0,0,0,0]:
            return 0
           
        freq = defaultdict(int)
        
        ans = len(s)
        
        left = 0
        
        for right in range(len(s)):
        
            freq[s[right]] += 1
            
            
            while left <= right and self.isBalancer(freq, excess):
                
                ans = min(ans, right - left+1)
                
                freq[s[left]]-=1
                left+=1
            
                
        return ans
            
            
            
            
    def isBalancer(self, freq, excess):
        
        for key in excess:
            if excess[key] > 0 and freq[key] < excess[key]: 
                return False
            
        return True
                
                
        
        
        
                
        
        