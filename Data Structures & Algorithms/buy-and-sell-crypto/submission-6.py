class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = prices[0]
        max_profit = 0

        for sell in prices:
            profit = sell - buy
            max_profit = max(profit, max_profit)
            buy = min(sell, buy)

        return max_profit