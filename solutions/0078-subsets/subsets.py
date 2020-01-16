# -*- coding:utf-8 -*-


# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
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
