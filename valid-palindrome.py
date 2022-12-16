class Solution(object):
    def isPalindrome(self, s):
        i, j = 0, len(s)-1
        while i < j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() == s[j].lower():
                    i+=1
                    j-=1
                else:
                    return False
            elif s[i].isalnum():
                j-=1
            else:
                i+=1
        return True
