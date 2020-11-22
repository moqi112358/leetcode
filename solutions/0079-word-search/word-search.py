# -*- coding:utf-8 -*-


# Given an m x n board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
#  
# Example 1:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
#
#
# Example 2:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
#
#
# Example 3:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
#
#
#  
# Constraints:
#
#
# 	m == board.length
# 	n = board[i].length
# 	1 <= m, n <= 200
# 	1 <= word.length <= 103
# 	board and word consists only of lowercase and uppercase English letters.
#
#


class Solution(object):
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if word is None:
            return True
        if board is None:
            return False
        visited = [[0] *len(board[0]) for k in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    k = visited[i][j]
                    visited[i][j] = 1
                    if self.word_detect(board, i, j, word[1:], visited):
                        return True
                    visited[i][j] = k
        return False
                    
    
    def word_detect(self, board, m, n, word, visited):
        #print(m,n,word,visited)
        if len(word) == 0:
            return True
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        for i in range(4):
            x = m + dx[i]
            y = n + dy[i]
            if  0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == word[0] and visited[x][y] == 0:
                k = visited[x][y]
                visited[x][y] = 1
                if self.word_detect(board, x, y, word[1:], visited):
                    return True
                visited[x][y] = k
        return False
    '''
    def exist(self, board, word):
        if not board:
            return False
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False
    
    # check whether can find word, start at (i,j) position    
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian 
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
        or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res
     '''   
        
