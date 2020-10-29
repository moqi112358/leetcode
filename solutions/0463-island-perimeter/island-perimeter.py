# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
#
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
#
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
#
#  
# Example 1:
#
#
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
#
#
# Example 2:
#
#
# Input: grid = [[1]]
# Output: 4
#
#
# Example 3:
#
#
# Input: grid = [[1,0]]
# Output: 4
#
#
#  
# Constraints:
#
#
# 	row == grid.length
# 	col == grid[i].length
# 	1 <= row, col <= 100
# 	grid[i][j] is 0 or 1.
#
#


#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#
# https://leetcode.com/problems/island-perimeter/description/
#
# algorithms
# Easy (61.65%)
# Total Accepted:    146.5K
# Total Submissions: 237.7K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# You are given a map in form of a two-dimensional integer grid where 1
# represents land and 0 represents water.
# 
# Grid cells are connected horizontally/vertically (not diagonally). The grid
# is completely surrounded by water, and there is exactly one island (i.e., one
# or more connected land cells).
# 
# The island doesn't have "lakes" (water inside that isn't connected to the
# water around the island). One cell is a square with side length 1. The grid
# is rectangular, width and height don't exceed 100. Determine the perimeter of
# the island.
# 
# 
# 
# Example:
# 
# 
# Input:
# [[0,1,0,0],
# ⁠[1,1,1,0],
# ⁠[0,1,0,0],
# ⁠[1,1,0,0]]
# 
# Output: 16
# 
# Explanation: The perimeter is the 16 yellow stripes in the image below:
# 
# 
# 
# 
#
class Solution:
    def islandPerimeter(self, grid):
        preimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                elif grid[i][j] == 1:
                    if i == 0 or grid[i-1][j] == 0:
                        preimeter += 1
                    if j == 0 or grid[i][j-1] == 0:
                        preimeter += 1
                    if i == len(grid)-1 or grid[i+1][j] == 0:
                        preimeter += 1
                    if j == len(grid[0])-1  or grid[i][j+1] == 0:
                        preimeter += 1
        return preimeter
                    
        


