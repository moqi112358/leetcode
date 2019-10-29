# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
#
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.
#
#  
# Example 1:
# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]
#
#  
# Constraints:
#
#
# 	arr1.length, arr2.length <= 1000
# 	0 <= arr1[i], arr2[i] <= 1000
# 	Each arr2[i] is distinct.
# 	Each arr2[i] is in arr1.
#
#


#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#
# https://leetcode.com/problems/relative-sort-array/description/
#
# algorithms
# Easy (66.17%)
# Total Accepted:    23.4K
# Total Submissions: 35.4K
# Testcase Example:  '[2,3,1,3,2,4,6,7,9,2,19]\n[2,1,4,3,9,6]'
#
# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all
# elements in arr2 are also in arr1.
# 
# Sort the elements of arr1 such that the relative ordering of items in arr1
# are the same as in arr2.  Elements that don't appear in arr2 should be placed
# at the end of arr1 in ascending order.
# 
# 
# Example 1:
# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]
# 
# 
# Constraints:
# 
# 
# arr1.length, arr2.length <= 1000
# 0 <= arr1[i], arr2[i] <= 1000
# Each arr2[i] is distinct.
# Each arr2[i] is in arr1.
# 
# 
#
class Solution:
    def relativeSortArray(self, arr1, arr2):
        set2 = set(arr2)
        not_in_arr2 = []
        arr1_arr2 = {}
        for i in arr1:
            if i in set2:
                arr1_arr2[i] = arr1_arr2.get(i, 0) + 1
            else:
                not_in_arr2.append(i)
        res = []
        for i in arr2:
            res.extend([i] * arr1_arr2[i])
        not_in_arr2.sort()
        res.extend(not_in_arr2)
        return res


