# A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
#
# For example, these are arithmetic sequences:
#
#
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
#
# The following sequence is not arithmetic.
#
#
# 1, 1, 2, 5, 7
#  
#
# A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.
#
# A slice (P, Q) of the array A is called arithmetic if the sequence:
# A[P], A[P + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.
#
# The function should return the number of arithmetic slices in the array A.
#  
#
# Example:
#
#
# A = [1, 2, 3, 4]
#
# return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
#
#


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if not A:
            return 0
        res = 0
        i = 0
        while i < len(A) - 2:
            if A[i+2] - A[i+1] == A[i+1] - A[i]:
                delta = A[i+1] - A[i]
                j = i + 3
                while j < len(A):
                    if A[j] - A[j-1] == delta:
                        j += 1
                    else:
                        break
                seq_length = j - i
                i = j
                res += (seq_length - 1) * (seq_length - 2) / 2
            else:
                i += 1
        return int(res)
                
        
        
