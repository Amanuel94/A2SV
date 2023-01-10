class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        if num % 3 == 0:

            return [num/3-1, num/3, num/3+1]
        else:
            return []
