class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        sell = 0
        buy = -prices[0]

        i = 1
        while i < len(prices):
            print(sell, buy)
            temp = sell
            sell = max(sell, prices[i]+buy-fee)
            buy = max(buy, temp-prices[i])
            i+=1
        return sell