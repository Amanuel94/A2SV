class Solution(object):
    def missingNumber(self, nums):
        max_num = max(nums)
        all = set(list(range(max_num)))
        nums = set(nums)
        return list(all.difference(nums))[0] if   list(all.difference(nums))  else max_num+1
