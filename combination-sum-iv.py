class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        """
        the number of ways to make target out of nums = sum(number of ways to make target - nums[i])        out of nums
        """
        nums.sort()
        partition_table = [0]*target

        for i in range(target):
            for num in nums:
                if num == i+1:
                    partition_table[i]+=1
                if i+1 - num > 0:
                    partition_table[i]+=partition_table[i-num]
                else:
                    break
        return partition_table[-1]