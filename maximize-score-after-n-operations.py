class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        gcds = defaultdict(list)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                gcds[(i,j)] =  math.gcd(nums[i], nums[j])
        
        n = len(nums)
        @cache
        def dp(mask):
            count = (n - mask.bit_count()) // 2
            ans = 0
            for i in range(n):
                for j in range(i+1,n):
                    if mask & 1 << i == 0 and mask & 1 << j == 0:
                        ans = max(ans, count*gcds[(i,j)]+ dp(mask | 1<<i | 1 << j))
            return ans
        return dp(0)