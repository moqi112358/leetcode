# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
#
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
#
#
# Input: a = "1010", b = "1011"
# Output: "10101"
#


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m, n = len(a) - 1, len(b) - 1
        tag = 0
        res = ''
        while m >= 0 and n >= 0:
            tmp = int(a[m]) + int(b[n]) + tag
            if tmp >= 2:
                tmp -= 2
                tag = 1
            else:
                tag = 0
            res = str(tmp) + res
            m -= 1
            n -= 1
        if m < 0:
            while n >= 0:
                tmp = int(b[n]) + tag
                if tmp >= 2:
                    tmp -= 2
                    tag = 1
                else:
                    tag = 0
                res = str(tmp) + res
                n -= 1
        if n < 0:
            while m >= 0:
                tmp = int(a[m]) + tag
                if tmp >= 2:
                    tmp -= 2
                    tag = 1
                else:
                    tag = 0
                res = str(tmp) + res
                m -= 1
        if tag == 1:
            res = '1' + res
        return res
