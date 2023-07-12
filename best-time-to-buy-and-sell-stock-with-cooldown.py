class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        profit if buy at i and sell at j = sellj-buyi + maxProfit(prices[i:]) 

        """

        # hold: -1 -1 -1 +1 +1 +1 +4 +5  
        # sell: +0 +2 +2 +2 +6 +6 +6 +6



        # n = len(prices)
        # dp = [0]*(n+2)
        # for i in range(n-2, -1, -1):
        #     for j in range(i+1, n):
        #         # max profit after day i
        #         dp[i] = max(
        #             dp[i],
        #             prices[j]-prices[i] + dp[j+2],
        #             dp[i+1]
        #         )
        # return dp[0]

        n = len(prices)

        if n < 2:
            return 0

        buy = [0]*n
        sell = [0]*n

        buy[0], buy[1] = -prices[0], max(-prices[1], -prices[0])
        sell[1] = max(buy[0]+prices[1], 0)

        for i in range(2, n):
            buy[i] = max(
                buy[i-1],
                sell[i-2]-prices[i],
                -prices[i-1]
            )
            sell[i] = max(
                sell[i-1],
                prices[i]+buy[i-1]
            )
        print(buy)
        print(sell)
        
        return sell[-1]