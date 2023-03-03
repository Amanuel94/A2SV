class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans  = [-1]*len(nums)
        stack = []
        
        nums = nums*2
        
        for i, num in enumerate(nums):
            if not stack or stack[-1][0] >= num:
                stack.append((num, i))
            else:
                while stack and stack[-1][0] < num:
                    x = stack.pop()
                    ans[x[1]%len(ans)] = num
                stack.append((num, i))
        return ans
        