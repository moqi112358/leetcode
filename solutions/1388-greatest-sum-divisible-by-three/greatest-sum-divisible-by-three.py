# -*- coding:utf-8 -*-


# Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.
#
#
#
#
#  
# Example 1:
#
#
# Input: nums = [3,6,5,1,8]
# Output: 18
# Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
#
# Example 2:
#
#
# Input: nums = [4]
# Output: 0
# Explanation: Since 4 is not divisible by 3, do not pick any number.
#
#
# Example 3:
#
#
# Input: nums = [1,2,3,4,4]
# Output: 12
# Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 4 * 10^4
# 	1 <= nums[i] <= 10^4
#
#


class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mod = 0
        min_mod11, min_mod12, min_mod21, min_mod22 = float('inf'), float('inf'), float('inf'), float('inf')
        for i in nums:
            if i % 3 == 1:
                mod += 1
                if i < min_mod11:
                    min_mod11, min_mod12 = i, min_mod11
                elif i < min_mod12:
                    min_mod12 = i
            elif i % 3 == 2:
                mod += 2
                if i < min_mod21:
                    min_mod21, min_mod22 = i, min_mod21
                elif i < min_mod22:
                    min_mod22 = i
        remove_mod = mod % 3
        s = sum(nums)
        if remove_mod == 0:
            return s
        if remove_mod == 1:
            if min_mod11 < min_mod21 + min_mod22:
                return s - min_mod11 if min_mod11 < s else 0
            else:
                return s - min_mod21 - min_mod22 if min_mod21 + min_mod22 < s else 0
        if remove_mod == 2:
            if min_mod21 < min_mod11 + min_mod12:
                return s - min_mod21 if min_mod21 < s else 0
            else:
                return s - min_mod11 - min_mod12 if min_mod11 + min_mod12 < s else 0
