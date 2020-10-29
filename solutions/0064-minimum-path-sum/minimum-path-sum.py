# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example:
#
#
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
#
#


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        res_matrix = [[0] * len(grid[0]) for _ in range(len(grid))]
        res_matrix[0][0] = grid[0][0]
        for i in range(1, len(grid[0])):
            res_matrix[0][i] = res_matrix[0][i-1] + grid[0][i] 
        for i in range(1, len(grid)):
            res_matrix[i][0] = res_matrix[i-1][0] + grid[i][0]
        for j in range(1, len(grid[0])):
            for i in range(1, len(grid)):
                res_matrix[i][j] = min(res_matrix[i-1][j], res_matrix[i][j-1]) + grid[i][j]
        return res_matrix[len(grid)-1][len(grid[0])-1]
