class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = set(nums)
        set_reversed = set(map(self.reverse_int, nums)) 
        return len(set_nums | set_reversed)
    
    def reverse_int(self, s):
        i = len(str(s))-1
        res = 0
        while s > 0:
            unit = s%10
            res += unit*(10**i)
            s = s//10
            i-=1
        return res