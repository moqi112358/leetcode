# Given a 2D board and a list of words from the dictionary, find all words in the board.
#
# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
#  
#
# Example:
#
#
# Input: 
# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]
#
# Output: ["eat","oath"]
#
#
#  
#
# Note:
#
#
# 	All inputs are consist of lowercase letters a-z.
# 	The values of words are distinct.
#
#


class Trie:
    def __init__(self):
        self.root = {}
        self.end = -1
    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node:
                node[w] = {}
                node = node[w]
            else:
                node = node[w]
        node[self.end] = True
    def search(self, word):
        node = self.root
        for w in word:
            if w not in node:
                return False
            node = node[w]
        if self.end not in node:
            return False
        else:
            return True
    def startWith(self, word):
        node = self.root
        for w in word:
            if w not in node:
                return False
            node = node[w]
        return True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words:
            return []
        prefixTree = Trie()
        for w in words:
            prefixTree.insert(w)
        res = set()
        
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                visited = [[False] * n for i in range(m)]
                visited[i][j] = True
                self.dfs(i, j, m, n, board, res, prefixTree, visited, board[i][j])
        return list(res)
    
    def dfs(self, i, j, m, n, board, res, prefixTree, visited, pre):
        dxy = [(0,1), (0,-1), (1,0), (-1,0)]
        if prefixTree.search(pre):
            res.add(pre)
        for d in dxy:
            x = i + d[0]
            y = j + d[1]
            if 0 <= x < m and 0 <= y < n and visited[x][y] is False and prefixTree.startWith(pre+board[x][y]):
                visited[x][y] = True
                self.dfs(x, y, m, n, board, res, prefixTree, visited, pre+board[x][y])
                visited[x][y] = False
