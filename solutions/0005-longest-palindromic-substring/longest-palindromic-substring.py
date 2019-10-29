# -*- coding:utf-8 -*-


# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: "cbbd"
# Output: "bb"
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
