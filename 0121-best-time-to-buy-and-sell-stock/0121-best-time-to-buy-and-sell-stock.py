class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low = prices[0]
        high = 0
        for i in range(1,len(prices)):
            if prices[i] < low: 
                low = prices[i]
            else: 
                high = max(high, prices[i]-low)

        return high
