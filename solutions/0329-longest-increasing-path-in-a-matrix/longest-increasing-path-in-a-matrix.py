# Given an integer matrix, find the length of the longest increasing path.
#
# From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
#
# Example 1:
#
#
# Input: nums = 
# [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ] 
# Output: 4 
# Explanation: The longest increasing path is [1, 2, 6, 9].
#
#
# Example 2:
#
#
# Input: nums = 
# [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ] 
# Output: 4 
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
#
#


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[1] * n for _ in range(m)] 
        for i in range(m):
            for j in range(n):
                self.dfs(i, j, matrix, dp, 0)
        return max([k for i in dp for k in i])
    
    def dfs(self, i, j, matrix, dp, length):
        if dp[i][j] > 1:
            return dp[i][j] 
        res = 1
        m, n = len(matrix), len(matrix[0])
        dxy = [(0,1),(0,-1),(1,0),(-1,0)]
        for d in dxy:
            dx, dy = d[0], d[1]
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and matrix[x][y] < matrix[i][j]:
                res = max(res, self.dfs(x, y, matrix, dp, length+1) + 1)
        dp[i][j] = res
        return dp[i][j]
    
