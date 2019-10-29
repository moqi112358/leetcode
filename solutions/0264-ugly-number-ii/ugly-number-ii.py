# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
#
# Example:
#
#
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
#
# Note:  
#
#
# 	1 is typically treated as an ugly number.
# 	n does not exceed 1690.
#


class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        s2, s3, s5 = 0, 0, 0
        result = [1]
        while n > 1:
            tmp = min(2 * result[s2], 3 * result[s3], 5 * result[s5])
            if tmp == 2 * result[s2]:
                s2 += 1
            if tmp == 3 * result[s3]:
                s3 += 1
            if tmp ==5 * result[s5]:
                s5 += 1
            result.append(tmp)
            n -= 1
        return result[-1]
