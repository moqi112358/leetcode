# Given a m * n matrix seats  that represent seats distributions in a classroom. If a seat is broken, it is denoted by '#' character otherwise it is denoted by a '.' character.
#
# Students can see the answers of those sitting next to the left, right, upper left and upper right, but he cannot see the answers of the student sitting directly in front or behind him. Return the maximum number of students that can take the exam together without any cheating being possible..
#
# Students must be placed in seats in good condition.
#
#  
# Example 1:
#
#
# Input: seats = [["#",".","#","#",".","#"],
#                 [".","#","#","#","#","."],
#                 ["#",".","#","#",".","#"]]
# Output: 4
# Explanation: Teacher can place 4 students in available seats so they don't cheat on the exam. 
#
#
# Example 2:
#
#
# Input: seats = [[".","#"],
#                 ["#","#"],
#                 ["#","."],
#                 ["#","#"],
#                 [".","#"]]
# Output: 3
# Explanation: Place all students in available seats. 
#
#
#
# Example 3:
#
#
# Input: seats = [["#",".",".",".","#"],
#                 [".","#",".","#","."],
#                 [".",".","#",".","."],
#                 [".","#",".","#","."],
#                 ["#",".",".",".","#"]]
# Output: 10
# Explanation: Place students in available seats in column 1, 3 and 5.
#
#
#  
# Constraints:
#
#
# 	seats contains only characters '.' and'#'.
# 	m == seats.length
# 	n == seats[i].length
# 	1 <= m <= 8
# 	1 <= n <= 8
#
#


# class Solution:
#     def maxStudents(self, seats: List[List[str]]) -> int:
#         if not seats:
#             return 0
#         return self.helper(seats)
        
#     def helper(self, seats):
#         import copy
#         res = 0
#         m, n = len(seats), len(seats[0])
#         dxy = [(0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
#         for i in range(m):
#             for j in range(n):
#                 if seats[i][j] == '#':
#                     continue
#                 elif seats[i][j] == '.':
#                     tmp = copy.deepcopy(seats) 
#                     # print('raw', seats)
#                     seats[i][j] = '#'
#                     for d in dxy:
#                         x, y = i + d[0], j + d[1]
#                         if 0 <= x < m and  0 <= y < n and seats[x][y] == '.':
#                             seats[x][y] = '#'
#                     res = max(res, 1 + self.helper(seats))
#                     seats = copy.deepcopy(tmp) 
#         return res
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        R, C = len(seats), len(seats[0])
        maxx = 2 ** R
        dp = [0] * maxx
        
        for c in range(C):
            n_dp = [0] * maxx
            for i in range(maxx):
                count = 0
                flag = False
                for k in range(R):
                    t = (1 << k) & i
                    if t:
                        count += 1
                    if t and seats[k][c] == '#':
                        flag = True
                if flag:
                    continue
                for j in range(maxx):
                    if ((i | (i >> 1)) & j) == 0 and ((j | j >> 1) & i == 0):
                        n_dp[i] = max(n_dp[i], dp[j] + count)
            dp = n_dp
        return max(dp)
