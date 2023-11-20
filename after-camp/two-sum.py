class Solution(object):
    def twoSum(self, nums, target):
        pair = []
        
        for i in range(len(nums)):
            if target - nums[i] in nums and nums.index(target - nums[i])!=i:
                    pair.append(i)
                    pair.append(nums.index(target - nums[i]))
                    return pair

                
        