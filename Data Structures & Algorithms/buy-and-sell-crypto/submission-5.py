# 26 Sep 26 Optimised
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]

        for i in range(1, len(prices)):
            sell = prices[i]
            max_profit = max(sell - buy, max_profit)
            buy = min(buy, sell)

        return max_profit
            



















# 26 Sep 26 (brute force)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit = 0
#         for i in range(len(prices)):
#             buy = prices[i]
#             for j in range(i + 1, len(prices)):
#                 sale = prices[j]
#                 profit = sale - buy
#                 max_profit = max(max_profit, profit)
#         return max_profit