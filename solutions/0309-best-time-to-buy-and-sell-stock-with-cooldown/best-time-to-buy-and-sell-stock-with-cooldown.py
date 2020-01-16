# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
#
#
# 	You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# 	After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
#
#
# Example:
#
#
# Input: [1,2,3,0,2]
# Output: 3 
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
#


class Solution:
#     Method1: dp[i][j] - result from day i to day j
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0
#         dp = [[0] * len(prices) for i in range(len(prices))]
#         for i in range(len(prices)):
#             for j in range(len(prices)):
#                 #calculate dp[j][i+j]
#                 if i + j <= len(prices) - 1:
#                     if i == 0:
#                         dp[j][i+j] = 0
#                     elif i == 1:
#                         dp[j][i+j] = max(0, prices[i+j] - prices[j])
#                     else:
#                         tmp_res = max(0, prices[i+j] - prices[j])
#                         # choose one day as cooldown
#                         for k in range(i+1):
#                             if k != i:
#                                 #print(dp[j][k+j-1] + dp[k+1+j][i+j], i, j, k)
#                                 tmp_res = max(tmp_res, dp[j][k+j-1] + dp[k+1+j][i+j])
#                                 dp[j][i+j] = tmp_res
#                             elif k == i:
#                                 #print(dp[j][k+j-1], i, j, k)
#                                 tmp_res = max(tmp_res, dp[j][k+j-1])
#                                 dp[j][i+j] = tmp_res
#         return dp[0][len(prices)-1]
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [[0] * 2 for i in range(len(prices) + 1)]
        # 0 - have a stock
        # 1 - do not have a stock
        dp[1][0] = -prices[0]
        for i in range(2, len(prices)+1):
            dp[i][0] = max(dp[i-2][1] - prices[i-1], dp[i-1][0])
            dp[i][1] = max(dp[i-1][0] + prices[i-1], dp[i-1][1])
        return max(dp[len(prices)][0], dp[len(prices)][1])
            
