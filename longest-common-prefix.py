class Solution(object):
    def longestCommonPrefix(self, strs):
        common = strs[0]
        for str in strs[1:]:
            i = 0
            while i < min(len(str), len(common)) and str[i] == common[i]:
                 i+=1
            
            common = common[:i]
        
        return common
