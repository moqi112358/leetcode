# -*- coding:utf-8 -*-


# A string of '0's and '1's is monotone increasing if it consists of some number of '0's (possibly 0), followed by some number of '1's (also possibly 0.)
#
# We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.
#
# Return the minimum number of flips to make S monotone increasing.
#
#  
#
#
# Example 1:
#
#
# Input: "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.
#
#
#
# Example 2:
#
#
# Input: "010110"
# Output: 2
# Explanation: We flip to get 011111, or alternatively 000111.
#
#
#
# Example 3:
#
#
# Input: "00011000"
# Output: 2
# Explanation: We flip to get 00000000.
#
#
#  
#
# Note:
#
#
# 	1 <= S.length <= 20000
# 	S only consists of '0' and '1' characters.
#
#
#
#


class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        zero_before = [0] * (len(S) + 1) # contain the current position
        one_before = [0] * (len(S) + 1)
        for i in range(len(S)):
            if i == 0:
                if S[i] == '0':
                    zero_before[i+1] = 1
                    one_before[i+1] = 0
                elif S[i] == '1':
                    zero_before[i+1] = 0
                    one_before[i+1] = 1
            else:
                if S[i] == '0':
                    zero_before[i+1] = 1 + zero_before[i]
                    one_before[i+1] = one_before[i]
                elif S[i] == '1':
                    zero_before[i+1] = zero_before[i]
                    one_before[i+1] = 1 + one_before[i]
        count_one = one_before[-1]
        count_zero = zero_before[-1]
        res = float('inf')
        for k in range(len(zero_before)):
            tmp = one_before[k] + (count_zero - zero_before[k])
            if tmp <= res:
                res = tmp
        return res
            
        
        
        
