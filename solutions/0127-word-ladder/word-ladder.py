# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
#
#
# 	Only one letter can be changed at a time.
# 	Each transformed word must exist in the word list.
#
#
# Note:
#
#
# 	Return 0 if there is no such transformation sequence.
# 	All words have the same length.
# 	All words contain only lowercase alphabetic characters.
# 	You may assume no duplicates in the word list.
# 	You may assume beginWord and endWord are non-empty and are not the same.
#
#
# Example 1:
#
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
#
#
# Example 2:
#
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
#
#
#
#
#


class Solution:
#     Method1: Bidirectional  BFS Time Limit Exceeded 
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        import string
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        wordSet = set(wordList)
        queue1 = {beginWord}
        queue2 = {endWord}
        step = 0
        while queue1 and queue2:
            step += 1
            if len(queue1) > len(queue2):
                queue2, queue1 = queue1, queue2
            queue = set()
            for word in queue1:
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        w = word[:i] + c + word[i+1:]
                        if w in queue2:
                            return step + 1
                        if w in wordSet:
                            queue.add(w)
                            wordSet.remove(w)
            queue1 = queue

        return 0


#     Method1: DFS Time Limit Exceeded 
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         wordSet = set(wordList)
#         self.res = len(wordList) + 1
#         if endWord not in wordSet:
#             return 0
#         self.dfs(beginWord, endWord, wordSet, 1)
#         return self.res if self.res != len(wordList) + 1 else 0
        
#     def dfs(self, start, endWord, wordSet, count):
#         if start == endWord:
#             self.res = min(self.res, count)
#         else:
#             for w in wordSet:
#                 if self.CheckChange(w, start):
#                     wordSet.remove(w)
#                     self.dfs(w, endWord, wordSet, count + 1)
#                     wordSet.add(w)

#     def CheckChange(self, word1, word2):
#         count = 0
#         for i in range(len(word1)):
#             if word1[i] != word2[i]:
#                 count += 1
#         return count == 1
        
