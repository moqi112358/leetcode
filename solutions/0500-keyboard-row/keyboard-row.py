# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.
#
# In the American keyboard:
#
#
# 	the first row consists of the characters "qwertyuiop",
# 	the second row consists of the characters "asdfghjkl", and
# 	the third row consists of the characters "zxcvbnm".
#
#
#  
# Example 1:
#
#
# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]
#
#
# Example 2:
#
#
# Input: words = ["omk"]
# Output: []
#
#
# Example 3:
#
#
# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]
#
#
#  
# Constraints:
#
#
# 	1 <= words.length <= 20
# 	1 <= words[i].length <= 100
# 	words[i] consists of English letters (both lowercase and uppercase). 
#
#


#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#
# https://leetcode.com/problems/keyboard-row/description/
#
# algorithms
# Easy (62.77%)
# Total Accepted:    94.4K
# Total Submissions: 150.4K
# Testcase Example:  '["Hello","Alaska","Dad","Peace"]'
#
# Given a List of words, return the words that can be typed using letters of
# alphabet on only one row's of American keyboard like the image below.
# 
# 
# 
# 
# 
# 
# Example:
# 
# 
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
# 
# 
# 
# 
# Note:
# 
# 
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.
# 
# 
#
class Solution:
    def findWords(self, words):
        row1 = set(list('qwertyuiop'))
        row2 = set(list('asdfghjkl'))
        row3 = set(list('zxcvbnm'))
        res = []
        for w in words:
            w_new = w.lower()
            flag = 1
            if w_new[0] in row1:
                for a in w_new:
                    if a not in row1:
                        flag = 0
            elif w_new[0] in row2:
                for a in w_new:
                    if a not in row2:
                        flag = 0
            elif w_new[0] in row3:
                for a in w_new:
                    if a not in row3:
                        flag = 0
            if flag == 1:
                res.append(w)
        return res
        


