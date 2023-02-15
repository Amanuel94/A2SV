class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        return list(map(int,list(str(eval("".join(list(map(str, num))) + "+" + str(k))))))
        