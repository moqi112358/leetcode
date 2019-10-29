# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).
#
# Example 1:
#
# Input: [3, 2, 1]
#
# Output: 1
#
# Explanation: The third maximum is 1.
#
#
#
# Example 2:
#
# Input: [1, 2]
#
# Output: 2
#
# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
#
#
#
# Example 3:
#
# Input: [2, 2, 3, 1]
#
# Output: 1
#
# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.
#
#


#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#
# https://leetcode.com/problems/third-maximum-number/description/
#
# algorithms
# Easy (29.37%)
# Total Accepted:    102.1K
# Total Submissions: 347.5K
# Testcase Example:  '[3,2,1]'
#
# Given a non-empty array of integers, return the third maximum number in this
# array. If it does not exist, return the maximum number. The time complexity
# must be in O(n).
# 
# Example 1:
# 
# Input: [3, 2, 1]
# 
# Output: 1
# 
# Explanation: The third maximum is 1.
# 
# 
# 
# Example 2:
# 
# Input: [1, 2]
# 
# Output: 2
# 
# Explanation: The third maximum does not exist, so the maximum (2) is returned
# instead.
# 
# 
# 
# Example 3:
# 
# Input: [2, 2, 3, 1]
# 
# Output: 1
# 
# Explanation: Note that the third maximum here means the third maximum
# distinct number.
# Both numbers with value 2 are both considered as second maximum.
# 
# 
#
class Solution:
    def thirdMax(self, nums):
        min_nums = min(nums)
        max1, max2, max3 = min_nums - 1, min_nums - 1, min_nums - 1
        for i in nums:
            if i > max1:
                max1, max2, max3 = i, max1, max2
            elif i > max2 and i < max1:
                max1, max2, max3 = max1, i, max2
            elif i > max3 and i < max2:
                max1, max2, max3 = max1, max2, i
        return max3 if max3 != min_nums - 1 else max1
        


