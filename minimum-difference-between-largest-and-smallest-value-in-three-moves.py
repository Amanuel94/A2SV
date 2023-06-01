class Solution:
    def minDifference(self, nums: List[int]) -> int:
        """
        sort and check all the 8 possible checks 
        """

        if len(nums) <= 3:
            return 0
        nums.sort()
        ans = float('inf')
        for i in range(8):
            l, r = 0, len(nums)-1
            for k in range(3):
                kth_bit = (1<<k)&i
                if kth_bit:
                    l+=1
                else:
                    r-=1
            ans = min(nums[r]-nums[l], ans)
        return ans