class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        i = 0
        n = len(strs)
        l = len(strs[0])
        ans  = 0

        while i < l:
            j = 0
            
            isSorted = True
            max_ord = float('-inf')
            while j < n:
                if ord(strs[j][i]) < max_ord:
                    isSorted = False
                    break
                else:
                    max_ord = ord(strs[j][i])
                j+=1
            i+=1
            ans += int(not isSorted)

        return ans
