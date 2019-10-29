# Given an array of 4 digits, return the largest 24 hour time that can be made.
#
# The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.
#
# Return the answer as a string of length 5.  If no valid time can be made, return an empty string.
#
#  
#
#
# Example 1:
#
#
# Input: [1,2,3,4]
# Output: "23:41"
#
#
#
# Example 2:
#
#
# Input: [5,5,5,5]
# Output: ""
#
#
#  
#
# Note:
#
#
# 	A.length == 4
# 	0 <= A[i] <= 9
#
#
#


class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        import itertools
        tmp = list(itertools.permutations(A,4))
        tmp = [1000 * i[0] + 100 * i[1] + 10 * i[2] + i[3] for i in tmp]
        tmp.sort()
        tmp = tmp[::-1]
        for i in tmp:
            time = str(i)
            if len(time) < 4:
                time = '0' * (4 - len(time)) + time
            hour = int(time[:2])
            minute = int(time[2:])
            if 0 <= hour <= 23 and 0 <= minute <= 59:
                return time[:2] + ':' + time[2:]
        return ''
