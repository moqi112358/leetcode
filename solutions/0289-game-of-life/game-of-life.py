# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
#
# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
#
#
# 	Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# 	Any live cell with two or three live neighbors lives on to the next generation.
# 	Any live cell with more than three live neighbors dies, as if by over-population..
# 	Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
#
#
# Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
#
# Example:
#
#
# Input: 
# [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1],
#   [0,0,0]
# ]
# Output: 
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]
#
#
# Follow up:
#
#
# 	Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
# 	In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
#
#


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dxy = [(1,0),(1,1),(1,-1),(0,1),(0,-1),(-1,1),(-1,-1),(-1,0)]
        # rule 1 and 3: 1->0: mark the origin 1 as -1
        # rule 4: 0-> 1: mark the origin 0  as 2
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                count_live = 0
                for d in dxy:
                    x = i + d[0]
                    y = j + d[1]
                    if 0 <= x < m and 0 <= y < n and board[x][y] != 2 :
                        count_live += abs(board[x][y])
                if board[i][j] == 0 and count_live == 3:
                    board[i][j] = 2
                if board[i][j] == 1 and (count_live < 2 or count_live > 3):
                    board[i][j] = -1
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1
        # For follow up2:if board is infinite(too large), use sparse matrix to store the original matrix
                    
                    
        
