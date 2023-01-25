class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        ref = {}
        for i, ch in enumerate(s):
            if ch in ref:
                ref[ch][1] = i
            else:
                ref[ch] = [i,i]
        ref = sorted(ref.values())
        res = [ref[0]]
        
        for interval in ref[1:]:
            if interval[0] > res[-1][1]:
                res.append(interval)
            elif interval[1] > res[-1][1]:
                res[-1][1]= interval[1]
        # print(res)
        return [x[1]-x[0]+1 for x in res]
                
                
        