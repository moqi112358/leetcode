# Given an array of integers A with even length, return true if and only if it is possible to reorder it such that A[2 * i + 1] = 2 * A[2 * i] for every 0 <= i < len(A) / 2.
#
#  
#
#
#
#
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: [3,1,3,6]
# Output: false
#
#
#
# Example 2:
#
#
# Input: [2,1,2,6]
# Output: false
#
#
#
# Example 3:
#
#
# Input: [4,-2,2,-4]
# Output: true
# Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
#
#
#
# Example 4:
#
#
# Input: [1,2,4,16,8,4]
# Output: false
#
#
#  
#
# Note:
#
#
# 	0 <= A.length <= 30000
# 	A.length is even
# 	-100000 <= A[i] <= 100000
#
#
#
#
#
#


class Solution:
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        A.sort()
        dict = {}
        for i in A:
            dict[i] = dict.get(i, 0) + 1
        while True:
            tmp_list = [i for i in dict if dict[i] > 0]
            if len(tmp_list) == 0:
                break
            tmp = min(tmp_list)
            dict[tmp] -= 1
            if tmp * 2 in dict and dict[tmp*2] > 0:
                dict[tmp*2] -= 1
            elif tmp / 2 in dict and dict[tmp/2] > 0:
                dict[tmp/2] -= 1
                
            else:
                return False
        return True
