class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:


        """
        sort the satisfaction array and take the suffix sum twice until it reaches negative
        """
        satisfaction.sort()
        i = len(satisfaction)-1
        suffix_arr = []
        suffix_sum = 0
        while i >= 0:
            suffix_sum+=satisfaction[i]
            suffix_arr.append(suffix_sum)
            i-=1
        pre = 0
        for suffix in suffix_arr:
            if suffix < 0:
                return pre
            pre+=suffix
        return pre