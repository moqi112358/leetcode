# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
#  
# Example 1:
# Input: x = 123
# Output: 321
# Example 2:
# Input: x = -123
# Output: -321
# Example 3:
# Input: x = 120
# Output: 21
# Example 4:
# Input: x = 0
# Output: 0
#
#  
# Constraints:
#
#
# 	-231 <= x <= 231 - 1
#
#


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            flag = -1
            x = -1 * x
        else:
            flag = 1
        s = list(str(x))
        s.reverse()
        res = int(''.join(s)) * flag
        return res if res < 2**31 - 1 and res > -1 * 2 ** 31 else 0
