# -*- coding:utf-8 -*-


# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
# 0 ≤ x, y < 231.
#
#
# Example:
#
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
#
# The above arrows point to positions where the corresponding bits are different.
#
#


class Solution(object):
    def hammingDistance(self, x, y):
        # write your code here
        a = str(bin(max(x,y))[2:])
        b = str(bin(min(x,y))[2:])
        b = '0' * (len(a) - len(b)) + b;
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
        return count
        
