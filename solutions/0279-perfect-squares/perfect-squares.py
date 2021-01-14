# Given an integer n, return the least number of perfect square numbers that sum to n.
#
# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
#
#  
# Example 1:
#
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
#
#
# Example 2:
#
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 104
#
#


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
