# -*- coding:utf-8 -*-


# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
#
# Example:
#
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
#
#
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.
#
# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
#


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        p = 1
        for i in range(len(nums)-1):
            p *= nums[i]
            res[i+1] = p
        p = 1
        for i in range(len(nums)-1,0,-1):
            p *= nums[i]
            res[i-1] *= p
        return res
        
