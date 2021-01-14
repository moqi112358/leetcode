# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
#
# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
#
# Input: word1 = “coding”, word2 = “practice”
# Output: 3
#
#
#
# Input: word1 = "makes", word2 = "coding"
# Output: 1
#
#
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
#


class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        res = len(words)
        last_word = ''
        last_index = 0
        for i in range(len(words)):
            if not(words[i] == word1 or words[i] == word2):
                continue
            if last_word == '':
                last_word = words[i]
                last_index = i
            if last_word != words[i]:
                res = min(res, i - last_index)
                last_word = words[i]
                last_index = i
            elif last_word == words[i]:
                last_index = i
        return res
