# You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.
#
# You can return the answer in any order.
#
#  
# Example 1:
#
#
# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.
#
#
# Example 2:
#
#
# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# Output: []
#
#
# Example 3:
#
#
# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# Output: [6,9,12]
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 104
# 	s consists of lower-case English letters.
# 	1 <= words.length <= 5000
# 	1 <= words[i].length <= 30
# 	words[i] consists of lower-case English letters.
#
#


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        import collections
        word_length = len(words[0])
        s_length = len(s)
        word_count = len(words)
        index = 0        
        word2index = {}
        index_count = {}
        s2index = [-1 for _ in s]
        for w in words:
            if w not in word2index:
                word2index[w] = index
                index += 1
            index_count[word2index[w]] = index_count.get(word2index[w], 0) + 1
        for i in range(s_length):
            w = s[i:i+word_length]
            if i+word_length <= s_length and s[i:i+word_length] in word2index:
                s2index[i] = word2index[w]
            else:
                s2index[i] = -1
        res = []
        for i in range(s_length - word_count * word_length + 1):
            if collections.Counter([s2index[i + j * word_length] for j in range(word_count)]) == index_count:
                res.append(i)
        return res
            
