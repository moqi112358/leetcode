# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
#
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
#
# Example 2:
#
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.


class Solution:
    # def numSquares(self, n: int) -> int:
    #     dp = [n] * (n + 1)
    #     for i in range(n+1):
    #         if i ** 2 <= n:
    #             dp[i ** 2] = 1
    #         j = 0
    #         while j ** 2 <= i:
    #             dp[i] = min(dp[i], dp[i - j ** 2] + 1)
    #             j += 1
    #     return dp[n]
    def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')]*n
        for i in range(1, n+1):
            dp[i] = min(dp[i-j*j] for j in range(1, int(i**0.5)+1)) + 1
        return dp[n]
