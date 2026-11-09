class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        sell = 1
        profit = 0
        for i, n in enumerate(prices):
            if buy> n:
                buy = n
            profit = max(profit, n - buy)
        return profit