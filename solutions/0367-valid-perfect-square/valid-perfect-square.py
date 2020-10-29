# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Follow up: Do not use any built-in library function such as sqrt.
#
#  
# Example 1:
# Input: num = 16
# Output: true
# Example 2:
# Input: num = 14
# Output: false
#
#  
# Constraints:
#
#
# 	1 <= num <= 2^31 - 1
#
#


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return 1
        i, j = 1, int(num/2) + 1
        while i < j:
            mid = int((i + j) / 2)
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                i = mid + 1
            elif mid ** 2 > num:
                j = mid
        return False
        
