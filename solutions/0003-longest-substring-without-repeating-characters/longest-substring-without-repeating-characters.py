# -*- coding:utf-8 -*-


# Given a string s, find the length of the longest substring without repeating characters.
#
#  
# Example 1:
#
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
# Example 2:
#
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
# Example 3:
#
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
#
# Example 4:
#
#
# Input: s = ""
# Output: 0
#
#
#  
# Constraints:
#
#
# 	0 <= s.length <= 5 * 104
# 	s consists of English letters, digits, symbols and spaces.
#
#


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        indexDict = dict()
        maxLength = 1
        head = -1
        for i in range(len(s)):
            if s[i] in indexDict and indexDict[s[i]] >= head:
                head = indexDict[s[i]]
            else:
                maxLength = max(maxLength, i - head)
            indexDict[s[i]] = i
        maxLength = max(maxLength, len(s) - head - 1)
        return maxLength
