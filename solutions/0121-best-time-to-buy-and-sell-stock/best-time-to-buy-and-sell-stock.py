# You are given an array prices for which prices[i] is the price of a given stock on the ith day.
#
# You are only permitted to complete at most one transaction. In other words, you can buy one and sell one share of the stock. You cannot sell a stock before you buy one.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#
#  
# Example 1:
#
#
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# The answer is not 7-1 = 6, as selling price needs to be larger than buying price.
#
# Example 2:
#
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
#
#
#  
# Constraints:
#
#
# 	1 <= prices.length <= 105
# 	0 <= prices[i] <= 104
#
#


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        global_max, local_min = 0, float('inf')
        for i in range(len(prices)):
            global_max = max(global_max, prices[i] - local_min)
            local_min = min(local_min, prices[i])
        return global_max    
        
