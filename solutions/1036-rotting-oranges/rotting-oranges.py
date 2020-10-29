# In a given grid, each cell can have one of three values:
#
#
# 	the value 0 representing an empty cell;
# 	the value 1 representing a fresh orange;
# 	the value 2 representing a rotten orange.
#
#
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
#
#  
#
#
# Example 1:
#
#
#
#
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
#
#
#
# Example 2:
#
#
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
#
#
#
# Example 3:
#
#
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
#
#
#  
#
# Note:
#
#
# 	1 <= grid.length <= 10
# 	1 <= grid[0].length <= 10
# 	grid[i][j] is only 0, 1, or 2.
#
#
#
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
