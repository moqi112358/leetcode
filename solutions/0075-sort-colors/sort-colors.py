# -*- coding:utf-8 -*-


# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Follow up:
#
#
# 	Could you solve this problem without using the library's sort function?
# 	Could you come up with a one-pass algorithm using only O(1) constant space?
#
#
#  
# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]
# Example 3:
# Input: nums = [0]
# Output: [0]
# Example 4:
# Input: nums = [1]
# Output: [1]
#
#  
# Constraints:
#
#
# 	n == nums.length
# 	1 <= n <= 300
# 	nums[i] is 0, 1, or 2.
#
#


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        bottom, mid, top = 0, 0, len(nums) - 1
        while mid <= top:
            if nums[mid] == 0:
                nums[bottom], nums[mid] = nums[mid], nums[bottom]
                bottom += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[top], nums[mid] = nums[mid], nums[top]
                top -= 1
        return nums
        
