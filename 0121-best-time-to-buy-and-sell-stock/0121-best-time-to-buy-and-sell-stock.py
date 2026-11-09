class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        profit = 0
        for n in prices:
            buy = min(buy,n)
            profit = max(profit, n - buy)
        return profit