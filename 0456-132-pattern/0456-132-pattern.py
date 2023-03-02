class Solution:
    def find132pattern(self, nums):
        stack, candidate = [], float('-inf')
        for num in reversed(nums):
            if num < candidate: return True
            while stack and stack[-1] < num:
                candidate = stack.pop()
            stack.append(num)
        return False