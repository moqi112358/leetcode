# -*- coding:utf-8 -*-


# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.
#
# Return the number of closed islands.
#
#  
# Example 1:
#
#
#
#
# Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation: 
# Islands in gray are closed because they are completely surrounded by water (group of 1s).
#
# Example 2:
#
#
#
#
# Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# Output: 1
#
#
# Example 3:
#
#
# Input: grid = [[1,1,1,1,1,1,1],
#                [1,0,0,0,0,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,1,0,1,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,0,0,0,0,1],
#                [1,1,1,1,1,1,1]]
# Output: 2
#
#
#  
# Constraints:
#
#
# 	1 <= grid.length, grid[0].length <= 100
# 	0 <= grid[i][j] <=1
#
#


class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        print(grid)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    res = self.dfs(grid, i, j)
                    if res == True:
                        count += 1
        return count
        
    def dfs(self, grid, i, j):
        if i != 0 and i != len(grid) - 1 and j != 0 and j != len(grid[0]) - 1:
            res = True
        else:
            res = False
        dx = [0,0,-1,1]
        dy = [-1,1,0,0]
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                if grid[x][y] == 0:
                    grid[x][y] = 1
                    # type 1
                    #tmp = self.dfs(grid, x, y)
                    #res = res and tmp
                    # type 2
                    res =  self.dfs(grid, x, y) and res
                    # type 3 python中and的判断方式（a = False and func(x), func 不会运行）
                    # res = res and self.dfs(grid, x, y)
        return res
