# -*- coding:utf-8 -*-


# Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
#
# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
#
# You may return any answer array that satisfies this condition.
#
#  
#
# Example 1:
#
#
# Input: [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
#
#
#  
#
# Note:
#
#
# 	2 <= A.length <= 20000
# 	A.length % 2 == 0
# 	0 <= A[i] <= 1000
#
#
#
#  
#


class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """       
        l = len(A) # l is even
        if l == 0:
            return A
        i, j = 0, l - 1 
        while i <= l - 1 and j >= 0:
            if A[i] % 2 == 0:
                i += 2
                continue
            if A[j] % 2 == 1:
                j -= 2
                continue
            if A[i] % 2 == 1 and A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
        return A
        
