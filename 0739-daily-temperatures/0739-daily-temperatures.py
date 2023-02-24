class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        stack = []
        ans = [0]*(len(temperatures))        
        
        for i, temp in enumerate(temperatures):
            k = 0
            while stack and stack[-1][0] < temp:
                a, b = stack.pop()
                ans[b] = i - b
            stack.append((temp, i))
        return ans
        
        