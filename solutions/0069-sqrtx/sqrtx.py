# Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
#
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
#
# Example 1:
#
#
# Input: 4
# Output: 2
#
#
# Example 2:
#
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
#              the decimal part is truncated, 2 is returned.
#
#


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        '''
        i, j = 0, int(x/2) + 1
        while i <= j:
            tmp = int((i+j)/2)
            if tmp ** 2 <= x < (tmp + 1) ** 2:
                return tmp
            elif x < tmp ** 2:
                j = tmp - 1
            elif x >= (tmp + 1) ** 2:
                i = tmp + 1
        return
        '''
        import math
        return int(math.sqrt(x))
