# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
#
# An obstacle and space is marked as 1 and 0 respectively in the grid.
#
#  
# Example 1:
#
#
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
#
#
# Example 2:
#
#
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
#
#
#  
# Constraints:
#
#
# 	m == obstacleGrid.length
# 	n == obstacleGrid[i].length
# 	1 <= m, n <= 100
# 	obstacleGrid[i][j] is 0 or 1.
#
#


class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         self.count = 0
#         if not obstacleGrid:
#             return self.count
#         m, n = len(obstacleGrid), len(obstacleGrid[0])
#         if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
#             return self.count
#         self.helper(obstacleGrid, 0, 0, m, n)
#         return self.count
        
#     def helper(self, obstacleGrid, r, c, m, n):
#         if r == m - 1 and c == n - 1:
#             self.count += 1
#             return
        
#         dx = [0, 1]
#         dy = [1, 0]
#         for i in range(2):
#             x = r + dx[i]
#             y = c + dy[i]
#             if 0 <= x <= m - 1 and 0 <= y <= n - 1 and obstacleGrid[x][y] != 1:
#                 self.helper(obstacleGrid, x, y, m, n)
#         return

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.count = 0
        if not obstacleGrid:
            return self.count
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return self.count
        res = [[0] * n for i in range(m)]
        
        value = 1
        for i in range(m):
            if obstacleGrid[i][0] != 1:
                res[i][0] = value
            else:
                value = 0
                res[i][0] = value
        
        value = 1
        for i in range(n):
            if obstacleGrid[0][i] != 1:
                res[0][i] = value
            else:
                value = 0
                res[0][i] = value
                
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    res[i][j] = res[i-1][j] + res[i][j-1]
        return res[m-1][n-1]
        
