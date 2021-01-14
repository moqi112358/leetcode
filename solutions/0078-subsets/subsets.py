# -*- coding:utf-8 -*-


# Given an integer array nums, return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets.
#
#  
# Example 1:
#
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
# Example 2:
#
#
# Input: nums = [0]
# Output: [[],[0]]
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 10
# 	-10 <= nums[i] <= 10
# 	All the numbers of nums are unique.
#
#


class Solution(object):
    '''
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        self.helper(nums, res, [])
        return res
    
    def helper(self, nums, res, cur):
        for i in range(len(nums)):
            res.append(cur + [nums[i]])
            self.helper(nums[i+1:], res, cur+[nums[i]])
    '''
    def subsets(self, nums):
        res = [[]]    
        for i in range(len(nums)):
            for j in range(len(res)):
                res.append(res[j] + [nums[i]])
        return res
