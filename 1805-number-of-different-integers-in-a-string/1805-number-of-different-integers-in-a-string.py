class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        s = ""
        for c in word:
            if c.isdigit():
                s = s+c
            else:
                s= s+" "
        integers = set(int(num) for num in s.split())
        return len(integers)