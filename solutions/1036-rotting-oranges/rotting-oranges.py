# You are given an m x n grid where each cell can have one of three values:
#
#
# 	0 representing an empty cell,
# 	1 representing a fresh orange, or
# 	2 representing a rotten orange.
#
#
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
#
#  
# Example 1:
#
#
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
#
#
# Example 2:
#
#
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
#
#
# Example 3:
#
#
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
#
#
#  
# Constraints:
#
#
# 	m == grid.length
# 	n == grid[i].length
# 	1 <= m, n <= 10
# 	grid[i][j] is 0, 1, or 2.
#
#


# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         if not grid:
#             return -1
#         iter_count = 0
#         while True:
#             count, count_fresh = self.update(grid)
#             if count != 0:
#                 iter_count += 1
#             else:
#                 if count_fresh == 0:
#                     return iter_count
#                 else:
#                     return -1
    
#     def update(self, grid):
#         count = 0
#         m, n = len(grid), len(grid[0])
#         dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 2:
#                     for d in dxy:
#                         x, y = i + d[0], j + d[1]
#                         if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
#                             count += 1
#                             grid[x][y] = 3
#         count_fresh = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 3:
#                     grid[i][j] = 2
#                 if grid[i][j] == 1:
#                     count_fresh += 1
#         return count, count_fresh

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        start = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    start.append((i, j, 0))
        last_iter = 0
        while start:
            node = start.popleft()
            i, j, iter_count = node[0], node[1], node[2]
            for d in dxy:
                x, y = i + d[0], j + d[1]
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    start.append((x, y, iter_count + 1))
                    grid[x][y] = 2
                    last_iter = iter_count + 1
        
        if any(1 in row for row in grid):
            return -1
        return last_iter
