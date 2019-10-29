# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
#
#
# Input: "hello"
# Output: "holle"
#
#
#
# Example 2:
#
#
# Input: "leetcode"
# Output: "leotcede"
#
#
# Note:
# The vowels does not include the letter "y".
#
#  
#


#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (42.01%)
# Total Accepted:    167.9K
# Total Submissions: 399.6K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and reverse only the vowels of
# a string.
# 
# Example 1:
# 
# 
# Input: "hello"
# Output: "holle"
# 
# 
# 
# Example 2:
# 
# 
# Input: "leetcode"
# Output: "leotcede"
# 
# 
# Note:
# The vowels does not include the letter "y".
# 
# 
# 
#
class Solution:
    def reverseVowels(self, s):
        s = list(s)
        V = set(['a','e','i','o','u','A','E','I','O','U'])
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] not in V:
                i += 1
                continue
            if s[j] not in V:
                j -= 1
                continue
            if s[i] in V and s[j] in V:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        res = ''.join(s)
        return res

