# -*- coding:utf-8 -*-


# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
#     ...
#
#
# Example 1:
#
#
# Input: "A"
# Output: 1
#
#
# Example 2:
#
#
# Input: "AB"
# Output: 28
#
#
# Example 3:
#
#
# Input: "ZY"
# Output: 701
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 7
# 	s consists only of uppercase English letters.
# 	s is between "A" and "FXSHRXW".
#
#


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {chr(x):x-64 for x in range(ord('A'),ord('Z')+1)}
        l = len(s)
        res = 0
        for c in s:
            res += dict[c] * (26 ** (l-1))
            l -= 1
        return res
