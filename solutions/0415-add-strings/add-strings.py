# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.
#
#


#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#
# https://leetcode.com/problems/add-strings/description/
#
# algorithms
# Easy (44.37%)
# Total Accepted:    109.9K
# Total Submissions: 247.7K
# Testcase Example:  '"0"\n"0"'
#
# Given two non-negative integers num1 and num2 represented as string, return
# the sum of num1 and num2.
# 
# Note:
# 
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#
class Solution:
    def addStrings(self, num1, num2):
        res = []
        if len(num1) < len(num2):
            num1 = '0' * ( len(num2) - len(num1) ) + num1
        else:
            num2 = '0' * ( len(num1) - len(num2) ) + num2
        i, j = len(num1) - 1, len(num2) - 1
        tmp = 0
        while i >= 0 and j >= 0:
            s = int(num1[i]) + int(num2[j]) + tmp
            if s >= 10:
                s -= 10
                tmp = 1
            else:
                tmp = 0
            res.append(str(s))
            i -= 1
            j -= 1
        if tmp == 1:
            res.append('1')
        res.reverse()
        return ''.join(res)
        
        


