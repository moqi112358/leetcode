# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
#
#  
# Example 1:
#
#
# Input: s = "abccccdd"
# Output: 7
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
#
#
# Example 2:
#
#
# Input: s = "a"
# Output: 1
#
#
# Example 3:
#
#
# Input: s = "bb"
# Output: 2
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 2000
# 	s consists of lowercase and/or uppercase English letters only.
#
#


#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (48.47%)
# Total Accepted:    105.8K
# Total Submissions: 217.9K
# Testcase Example:  '"abccccdd"'
#
# Given a string which consists of lowercase or uppercase letters, find the
# length of the longest palindromes that can be built with those letters.
# 
# This is case sensitive, for example "Aa" is not considered a palindrome
# here.
# 
# Note:
# Assume the length of given string will not exceed 1,010.
# 
# 
# Example: 
# 
# Input:
# "abccccdd"
# 
# Output:
# 7
# 
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# 
# 
#
class Solution:
    def longestPalindrome(self, s):
        hash_c = {};
        for i in s:
            hash_c[i] = hash_c.get(i,0) + 1
        flag = 0
        count = 0
        for i in hash_c:
            if hash_c[i] % 2 == 0:
                count += hash_c[i]
            else:
                count += hash_c[i] - 1
                flag = 1
        if flag == 1:
            count += 1
        return count


