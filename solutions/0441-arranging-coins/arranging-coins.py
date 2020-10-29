# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
#
# Given n, find the total number of full staircase rows that can be formed.
#
# n is a non-negative integer and fits within the range of a 32-bit signed integer.
#
# Example 1:
#
# n = 5
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
#
# Because the 3rd row is incomplete, we return 2.
#
#
#
# Example 2:
#
# n = 8
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
#
# Because the 4th row is incomplete, we return 3.
#
#


#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#
# https://leetcode.com/problems/arranging-coins/description/
#
# algorithms
# Easy (38.51%)
# Total Accepted:    76.3K
# Total Submissions: 198K
# Testcase Example:  '5'
#
# You have a total of n coins that you want to form in a staircase shape, where
# every k-th row must have exactly k coins.
# ⁠
# Given n, find the total number of full staircase rows that can be formed.
# 
# n is a non-negative integer and fits within the range of a 32-bit signed
# integer.
# 
# Example 1:
# 
# n = 5
# 
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
# 
# Because the 3rd row is incomplete, we return 2.
# 
# 
# 
# Example 2:
# 
# n = 8
# 
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
# 
# Because the 4th row is incomplete, we return 3.
# 
# 
#
# class Solution:
#     def arrangeCoins(self, n):
#         n = 2 * n
#         i = 1
#         # while i * (i + 1) <= n:
#         #     i += 1
#         # return i - 1
#         i, j = 0, n
#         while i < j:
#             m = int((i+j)/2)
#             if m * (m+1) <= n:
#                 i = m + 1
#             elif m * (m+1) > n:
#                 j = m - 1
#         return i if i  * (i + 1) <= n else i - 1
class Solution:
    def arrangeCoins(self, n):
        n = 2 * n
        import math
        # while i * (i + 1) <= n:
        #     i += 1
        # return i - 1
        res = int(math.sqrt(n))
        return res - 1 if res * (res + 1) > n else res 



