# Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.
#
# 24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.
#
# Return the latest 24-hour time in "HH:MM" format.  If no valid time can be made, return an empty string.
#
#  
# Example 1:
#
#
# Input: A = [1,2,3,4]
# Output: "23:41"
# Explanation: The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". Of these times, "23:41" is the latest.
#
#
# Example 2:
#
#
# Input: A = [5,5,5,5]
# Output: ""
# Explanation: There are no valid 24-hour times as "55:55" is not valid.
#
#
# Example 3:
#
#
# Input: A = [0,0,0,0]
# Output: "00:00"
#
#
# Example 4:
#
#
# Input: A = [0,0,1,0]
# Output: "10:00"
#
#
#  
# Constraints:
#
#
# 	arr.length == 4
# 	0 <= arr[i] <= 9
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
