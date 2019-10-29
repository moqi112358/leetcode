# Given an array A of 0s and 1s, divide the array into 3 non-empty parts such that all of these parts represent the same binary value.
#
# If it is possible, return any [i, j] with i+1 < j, such that:
#
#
# 	A[0], A[1], ..., A[i] is the first part;
# 	A[i+1], A[i+2], ..., A[j-1] is the second part, and
# 	A[j], A[j+1], ..., A[A.length - 1] is the third part.
# 	All three parts have equal binary value.
#
#
# If it is not possible, return [-1, -1].
#
# Note that the entire part is used when considering what binary value it represents.  For example, [1,1,0] represents 6 in decimal, not 3.  Also, leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.
#
#  
#
# Example 1:
#
#
# Input: [1,0,1,0,1]
# Output: [0,3]
#
#
#
# Example 2:
#
#
# Input: [1,1,0,1,1]
# Output: [-1,-1]
#
#
#  
#
# Note:
#
#
# 	3 <= A.length <= 30000
# 	A[i] == 0 or A[i] == 1
#
#
#
#  
#


class Solution:
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        count_one = A.count(1)
        if count_one % 3 != 0:
            return [-1,-1]
        exact_one = count_one / 3
        if exact_one == 0:
            return [0, 2]
        count_last_zero = 0
        for i in range(len(A)-1,-1,-1):
            if A[i] == 0:
                count_last_zero += 1
            elif A[i] == 1:
                break
        count_one = 0
        first_part_end, second_part_begin, second_part_end, third_part_begin = 0, 0, 0, 0
        for i in range(len(A)):
            if A[i] == 1:
                count_one += 1
                if count_one == exact_one:
                    first_part_end = i
                if count_one == exact_one + 1:
                    second_part_begin = i
                if count_one == exact_one * 2:
                    second_part_end = i
                if count_one == exact_one * 2 + 1:
                    third_part_begin = i
        B = [str(i) for i in A]
        if second_part_begin - first_part_end - 1 < count_last_zero or third_part_begin - second_part_end - 1 < count_last_zero:
            return [-1, -1]
        else:
            m, n = first_part_end+count_last_zero,second_part_end+count_last_zero+1
            if int(''.join(B[:m+1]),2) == int(''.join(B[n:]),2) and int(''.join(B[:m+1]),2) == int(''.join(B[m+1:n]),2):
                return [m, n]
            else:
                return [-1, -1]        
