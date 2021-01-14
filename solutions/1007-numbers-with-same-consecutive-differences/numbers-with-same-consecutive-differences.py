# Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.
#
# Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.
#
# You may return the answer in any order.
#
#  
# Example 1:
#
#
# Input: n = 3, k = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading zeroes.
#
#
# Example 2:
#
#
# Input: n = 2, k = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
#
#
# Example 3:
#
#
# Input: n = 2, k = 0
# Output: [11,22,33,44,55,66,77,88,99]
#
#
# Example 4:
#
#
# Input: n = 2, k = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
#
#
# Example 5:
#
#
# Input: n = 2, k = 2
# Output: [13,20,24,31,35,42,46,53,57,64,68,75,79,86,97]
#
#
#  
# Constraints:
#
#
# 	2 <= n <= 9
# 	0 <= k <= 9
#
#


class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        n = 1
        res = [i for i in range(10)]
        while n < N:
            tmp = []
            for i in res:
                self.addOne(i, K, tmp)
            res = tmp
            n += 1
        return res
    
    def addOne(self, num, K, res):
        s = str(num)
        last_digit = int(s[-1])
        for i in range(10):
            if abs(i - last_digit) == K:
                new = s + str(i)
                if self.helper(new):
                    res.append(int(new))
    
    def helper(self, num):
        if num[0] == '0' and len(num) > 1:
            return False
        return True
