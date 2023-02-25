class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        
        occ1 = Counter(s1)
        occ2 = Counter(s2[:len(s1)])
        if occ1 == occ2:
            return True
        
        for i in range(len(s1), len(s2)):
            occ2[s2[i-len(s1)]] -= 1
            if occ2[s2[i-len(s1)]] == 0:
                del occ2[s2[i-len(s1)]]
            occ2[s2[i]] = occ2.get(s2[i], 0) + 1
            if occ1 == occ2:
                return True
        
        return False
