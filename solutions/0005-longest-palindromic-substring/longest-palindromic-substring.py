# -*- coding:utf-8 -*-


# Given a string s, return the longest palindromic substring in s.
#
#  
# Example 1:
#
#
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: s = "cbbd"
# Output: "bb"
#
#
# Example 3:
#
#
# Input: s = "a"
# Output: "a"
#
#
# Example 4:
#
#
# Input: s = "ac"
# Output: "a"
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 1000
# 	s consist of only digits and English letters (lower-case and/or upper-case),
#
#


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_s = []
        for char in s:
            new_s.append('#')
            new_s.append(char)
        new_s.append('#')
        
        max_right = 0
        pos = 0
        max_len = 0
        radius = [0 for _ in xrange(len(new_s))]
        for i, char in enumerate(new_s):
            if i < max_right:
                radius[i] = min(radius[pos-(i-pos)], max_right - i)
            else:
                radius[i] = 1
                
            # Expand radius[i]
            self.expand(radius, i, new_s)
            
            # Update max_right, pos
            if i + radius[i] - 1 > max_right:
                max_right = i + radius[i] - 1
                pos = i
                
            # Update max_len
            if max_len < radius[i]:
                max_len = radius[i]
                mid = i
                
        max_len = max_len - 1
        start = (mid - 1) // 2 - (max_len - 1) // 2
        return s[start:start + max_len]
    
    def expand(self, radius, i, s):
        while i - radius[i] >= 0 and i + radius[i] < len(s) and s[i-radius[i]] == s[i+radius[i]]:
            radius[i] += 1
