# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words such that:
#
#
# 	The first word in the sequence is beginWord.
# 	The last word in the sequence is endWord.
# 	Only one letter is different between each adjacent pair of words in the sequence.
# 	Every word in the sequence is in wordList.
#
#
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
#
#  
# Example 1:
#
#
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog" with 5 words.
#
#
# Example 2:
#
#
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no possible transformation.
#
#
#  
# Constraints:
#
#
# 	1 <= beginWord.length <= 100
# 	endWord.length == beginWord.length
# 	1 <= wordList.length <= 5000
# 	wordList[i].length == beginWord.length
# 	beginWord, endWord, and wordList[i] consist of lowercase English letters.
# 	beginWord != endWord
# 	All the strings in wordList are unique.
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
        
