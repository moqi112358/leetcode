# -*- coding:utf-8 -*-


# Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.
#
# Example:
#
# Input:
# [1,2,3]
#
# Output:
# 3
#
# Explanation:
# Only three moves are needed (remember each move increments two elements):
#
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
#
#


class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        s = sum(nums)
        l = len(nums)
        minimum = min(nums)
        maximum = max(nums)
        n = 0
        while True:
            if (s + (l - 1) * n) % l == 0:
                m = (s + (l - 1) * n) / l
                if m - n <= minimum and m >= maximum:
                    return n
            n += 1
        '''
        return sum(nums) - len(nums)*min(nums)
