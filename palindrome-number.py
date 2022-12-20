class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0 and int(str(x)[::-1]) == x:
            return True
        else:
            return False
