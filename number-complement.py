class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        l = len(bin(num))-2
        balancer = ~(~0 << l)
        return ~num & balancer
