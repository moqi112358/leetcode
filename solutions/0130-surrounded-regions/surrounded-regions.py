# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# Example:
#
#
# X X X X
# X O O X
# X X O X
# X O X X
#
#
# After running your function, the board should be:
#
#
# X X X X
# X X X X
# X X X X
# X O X X
#
#
# Explanation:
#
# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
#


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return None
        m, n = len(board), len(board[0])
        for i in range(m):
            if board[i][0] == 'O':
                self.dfs(i,0,m,n,board)
            if board[i][n-1] == 'O':
                self.dfs(i,n-1,m,n,board)
        for i in range(n):
            if board[0][i] == 'O':
                self.dfs(0,i,m,n,board)
            if board[m-1][i] == 'O':
                self.dfs(m-1,i,m,n,board)
        print(board)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 0:
                    board[i][j] = 'O'
        
    def dfs(self, x, y, m, n, board):
        board[x][y] = 0
        dxy = [(1,0), (-1,0), (0,1), (0,-1)]
        for d in dxy:
            i = x + d[0]
            j = y + d[1]
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                self.dfs(i, j, m, n, board)
