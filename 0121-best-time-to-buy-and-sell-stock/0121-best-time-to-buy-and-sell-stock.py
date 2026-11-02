class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low = prices[0]
        profit = 0
        for p in prices:
            low = min(low, p)
            profit = max(profit, p-low)
        return profit
