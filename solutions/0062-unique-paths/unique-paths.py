# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#
#
# Above is a 7 x 3 grid. How many possible unique paths are there?
#
# Note: m and n will be at most 100.
#
# Example 1:
#
#
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
#
#
# Example 2:
#
#
# Input: m = 7, n = 3
# Output: 28
#


class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         self.count = 0
#         self.searchPath(m, n, 0, 0)
#         return self.count 
    
#     def searchPath(self, m, n, r, c):
#         if r == m - 1 and c == n - 1:
#             self.count += 1
#         dx = [0, 1]
#         dy = [1, 0]
#         for i in range(2):
#             x = r + dx[i]
#             y = c + dy[i]
#             if 0 <= x <= m - 1 and 0 <= y <= n - 1:
#                 self.searchPath(m, n, x, y)
#         return            
        
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0] * m for i in range(n)]
        for i in range(m):
            res[0][i] = 1
        for i in range(n):
            res[i][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                res[i][j] = res[i-1][j] + res[i][j-1]
        return res[n-1][m-1]
