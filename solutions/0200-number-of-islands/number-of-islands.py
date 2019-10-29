# -*- coding:utf-8 -*-


# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
#
#
# Example 2:
#
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3
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
