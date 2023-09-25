class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        n = len(stones)
        # 1 = ((-2+4)-1)-(-7+8)+1 = -2+4-1+7-8+1
        @cache
        def dp(pos, res):

            if pos == n:
                return res if res >= 0 else float('inf')

            return min(
                float('inf'),
                dp(pos+1, res-stones[pos]),
                dp(pos+1, res+stones[pos])
            )

        return dp(0, 0)