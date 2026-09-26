class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sale = prices[j]
                profit = sale - buy
                max_profit = max(max_profit, profit)
        return max_profit