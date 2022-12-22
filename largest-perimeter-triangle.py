class Solution(object):
    def largestPerimeter(self, nums):
        nums = sorted(nums, reverse=True)
        def areValid(x, y, z):
            return x+y > z
        
        i= 0
        while i < len(nums)-2:
            if areValid(nums[i+2], nums[i+1], nums[i]):
                return sum(nums[i:i+3])
            i+=1
        return 0
