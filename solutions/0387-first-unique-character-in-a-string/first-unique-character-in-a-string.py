# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
#
# Examples:
#
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode"
# return 2.
#
#
#  
#
# Note: You may assume the string contains only lowercase English letters.
#


class Solution:
    def firstUniqChar(self, s: str) -> int:
        h = {}
        for i in s:
            h[i] = h.get(i, 0) + 1
        for i in range(len(s)):
            if h[s[i]] == 1:
                return i
        return -1
        
