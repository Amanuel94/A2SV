class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}
        def dp(ptr, target):

            
            if (ptr, target) in memo:
                return memo[(ptr, target)]
            if target == 0:
                return 0
            if ptr == -1 or target < 0:
                return float('inf')
            
            memo[(ptr, target)] =min(dp(ptr-1,target),dp(ptr, target-coins[ptr])+1)
            return memo[(ptr, target)]
            
        
        return (lambda x: -1 if x == float('inf') else x)(dp(len(coins)-1, amount))