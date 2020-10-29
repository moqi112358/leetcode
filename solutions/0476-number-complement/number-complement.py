# Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.
#
#  
# Example 1:
#
#
# Input: num = 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
#
#
# Example 2:
#
#
# Input: num = 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
#
#
#  
# Constraints:
#
#
# 	The given integer num is guaranteed to fit within the range of a 32-bit signed integer.
# 	num >= 1
# 	You could assume no leading zero bit in the integer’s binary representation.
# 	This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/
#
#


#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#
# https://leetcode.com/problems/number-complement/description/
#
# algorithms
# Easy (62.69%)
# Total Accepted:    114.1K
# Total Submissions: 182K
# Testcase Example:  '5'
#
# Given a positive integer, output its complement number. The complement
# strategy is to flip the bits of its binary representation.
# 
# Note:
# 
# The given integer is guaranteed to fit within the range of a 32-bit signed
# integer.
# You could assume no leading zero bit in the integer’s binary
# representation.
# 
# 
# 
# Example 1:
# 
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits),
# and its complement is 010. So you need to output 2.
# 
# 
# 
# Example 2:
# 
# Input: 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and
# its complement is 0. So you need to output 0.
# 
# 
#
class Solution:
    def findComplement(self, num):
        s = bin(num)
        s = s[2:]
        t = ''
        for i in s:
            if i == '0':
                t += '1'
            else:
                t += '0'
        return int(t, 2)


