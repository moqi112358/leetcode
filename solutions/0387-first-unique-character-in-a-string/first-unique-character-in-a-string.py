#
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
#
#
#
#
# Note: You may assume the string contain only lowercase letters.
#


class Solution:
    def firstUniqChar(self, s: str) -> int:
        h = {}
        for i in s:
            h[i] = h.get(i, 0) + 1
        t = set()
        for i in h:
            if h[i] == 1:
                t.add(i)
        for i in range(len(s)):
            if s[i] in t:
                return i
        return -1
        
