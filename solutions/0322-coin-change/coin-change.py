# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
# Example 1:
#
#
# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1
#
# Example 2:
#
#
# Input: coins = [2], amount = 3
# Output: -1
#
#
# Note:
# You may assume that you have an infinite number of each kind of coin.
#


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[0]+[float('inf')]*amount
        for i in range(min(coins),amount+1):
            dp[i]=min([dp[i-coin] for coin in coins if coin<=i] )+1
        return dp[amount] if dp[amount]!=float('inf') else -1
    '''
    if amount == 0: return 0
    dp = [0] + [amount + 1] * amount
    for i in range(1, amount+1):
        if i in coins:
            dp[i] = 1
        else:
            for j in coins:
                if i >= j:
                    dp[i] = min(dp[i - j] + 1, dp[i])
    if dp[-1] == amount + 1:
        return -1
    return dp[-1]
    '''
