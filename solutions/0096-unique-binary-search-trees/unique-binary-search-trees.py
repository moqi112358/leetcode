# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
#
# Example:
#
#
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 19
#
#


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        self.helper(n, dp)
        print(dp)
        return dp[-1]
    
    def helper(self, n, dp):
        if dp[n] != 0 or n == 0:
            return dp[n]
        res = 0
        for i in range(n):
            left = self.helper(i, dp)
            right = self.helper(n - i - 1, dp)
            res += (left * right)
        dp[n] = res
        return dp[n]
            
            
