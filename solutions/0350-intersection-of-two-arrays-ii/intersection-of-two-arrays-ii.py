# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
#
#
#
# Example 2:
#
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
#
#
# Note:
#
#
# 	Each element in the result should appear as many times as it shows in both arrays.
# 	The result can be in any order.
#
#
# Follow up:
#
#
# 	What if the given array is already sorted? How would you optimize your algorithm?
# 	What if nums1's size is small compared to nums2's size? Which algorithm is better?
# 	What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
#
#


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h1, h2 = {}, {}
        for i in nums1:
            h1[i] = h1.get(i, 0) + 1
        '''
        for i in nums2:
            h2[i] = h2.get(i, 0) + 1
        res = []
        for i in h1:
            if i in h2:
                c = min(h1[i], h2[i])
                res.extend([i] * c)
        return res
        '''
        res = []
        for i in nums2:
            if i in h1 and h1[i] > 0:
                res.append(i)
                h1[i] -= 1
        return res
