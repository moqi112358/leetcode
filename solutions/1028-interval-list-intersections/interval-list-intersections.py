# Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
#
# Return the intersection of these two interval lists.
#
# (Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)
#
#
#  
#
# Example 1:
#
#
#
#
# Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
#
#
#  
#
# Note:
#
#
# 	0 <= A.length < 1000
# 	0 <= B.length < 1000
# 	0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
#
#
#


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []
        i, j = 0, 0
        res = []
        while i < len(A) and j < len(B):
            i, j = self.helper(A, B, i, j, res)
        return res
    
    def helper(self, A, B, i, j, res):
        a, b = A[i], B[j]
        if a[0] > b[1]:
            j += 1
        elif a[1] < b[0]:
            i += 1
        else:
            start, end = max(a[0], b[0]), min(a[1], b[1])
            if end >= start:
                res.append([start, end])
            if a[1] >= b[1]:
                j += 1
            else:
                i += 1
        return i, j
        
        
