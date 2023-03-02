class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        nums = nums[::-1]
        
        stack = []
        cur_2 = float('-inf')
        
        for num in nums:
            
            if cur_2 > num:
                return True
            while stack and stack[-1] < num:
                cur_2 =  stack.pop()
            stack.append(num)
        return False
        