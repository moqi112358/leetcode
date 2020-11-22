# Given two binary strings a and b, return their sum as a binary string.
#
#  
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#  
# Constraints:
#
#
# 	1 <= a.length, b.length <= 104
# 	a and b consist only of '0' or '1' characters.
# 	Each string does not contain leading zeros except for the zero itself.
#
#


class Solution:
    def addBinary(self, a: str, b: str) -> str:
#         l = max(len(a), len(b))
#         a = "0" * (l - len(a)) + a
#         b = "0" * (l - len(b)) + b
#         c = 0
#         res = ""
#         for i in range(l-1, -1, -1):
#             tmp = int(a[i]) + int(b[i]) + c
#             if tmp >= 2:
#                 tmp -= 2
#                 c = 1
#             else:
#                 c = 0
#             res += str(tmp)
#         if c == 1:
#             res += "1"
#         return res[::-1]
        res = int(a, 2) + int(b, 2)
        return str(bin(res))[2:]
            
