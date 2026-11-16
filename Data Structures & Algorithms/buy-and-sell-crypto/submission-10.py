class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        for sell in prices:
            max_profit = max(sell - buy, max_profit)
            buy = min(sell, buy)
        return max_profit