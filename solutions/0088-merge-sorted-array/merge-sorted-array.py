# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
#
#
# 	The number of elements initialized in nums1 and nums2 are m and n respectively.
# 	You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
#
#
# Example:
#
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]
#
#
#  
# Constraints:
#
#
# 	-10^9 <= nums1[i], nums2[i] <= 10^9
# 	nums1.length == m + n
# 	nums2.length == n
#
#


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            nums1[0:n] = nums2[0:n]
            return
        i = m + n - 1
        index_1 = m - 1
        index_2 = n - 1
        while index_1 >= 0 and index_2 >= 0:
            if nums1[index_1] < nums2[index_2]:
                nums1[i] = nums2[index_2]
                index_2 -= 1
            elif  nums1[index_1] >= nums2[index_2]:
                nums1[i] = nums1[index_1]
                index_1 -= 1
            i -= 1
        if index_1 < 0:
            nums1[0:index_2+1] = nums2[0:index_2+1]
        return 

