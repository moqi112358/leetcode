# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
#
# Example:
#
#
# Input: 
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Output: 4
#


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        res = 0
        dp = [[0] * (n+1) for _  in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == "0":
                    dp[i][j] == 0
                elif matrix[i-1][j-1] == "1":
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    res = max(res, dp[i][j])
        return res * res
        
