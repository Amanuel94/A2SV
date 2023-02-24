class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        uniques = defaultdict(int)
        ans = 0
        
        for right in range(len(s)):
            uniques[s[right]]+=1
            while not self.checkUnique(uniques):
                uniques[s[left]]-=1
                left+=1
            ans = max(right-left+1, ans)
        return ans
            
    def checkUnique(self, d):
        for key in d:
            if d[key] > 1:
                return False
        return True
    