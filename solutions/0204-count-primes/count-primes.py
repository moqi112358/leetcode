# Count the number of prime numbers less than a non-negative number, n.
#
#  
# Example 1:
#
#
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#
#
# Example 2:
#
#
# Input: n = 0
# Output: 0
#
#
# Example 3:
#
#
# Input: n = 1
# Output: 0
#
#
#  
# Constraints:
#
#
# 	0 <= n <= 5 * 106
#
#


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 0
        res = [True] * n
        res[0] = res[1] = False
        for i in range(2,int(n**0.5)+1):
            res[i*i:(n+1):i] = [False] * len(res[i*i:(n+1):i])
        return sum(res)
