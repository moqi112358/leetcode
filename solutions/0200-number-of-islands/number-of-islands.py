# -*- coding:utf-8 -*-


# Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
#  
# Example 1:
#
#
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#
#
# Example 2:
#
#
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
#
#  
# Constraints:
#
#
# 	m == grid.length
# 	n == grid[i].length
# 	1 <= m, n <= 300
# 	grid[i][j] is '0' or '1'.
#
#


class Solution:
    def numIslands(self, grid):
        if not grid: return 0

        def isValid(x, y):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
                return True
            else:
                return False

        def dfs(x, y):
            if grid[x][y] == -1:
                return

            grid[x][y] = -1
            shifts = {(0,1), (1,0), (0,-1), (-1,0)}
            for s in shifts:
                new_x, new_y = x + s[0], y + s[1]
                if isValid(new_x, new_y):
                    dfs(new_x, new_y)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)

        return count
