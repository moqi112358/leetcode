# Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:
#
#
# 	perm[i] is divisible by i.
# 	i is divisible by perm[i].
#
#
# Given an integer n, return the number of the beautiful arrangements that you can construct.
#
#  
# Example 1:
#
#
# Input: n = 2
# Output: 2
# Explanation: 
# The first beautiful arrangement is [1,2]:
#     - perm[1] = 1 is divisible by i = 1
#     - perm[2] = 2 is divisible by i = 2
# The second beautiful arrangement is [2,1]:
#     - perm[1] = 2 is divisible by i = 1
#     - i = 2 is divisible by perm[2] = 1
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 1
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 15
#
#


class Solution(object):
    def countArrangement(self, N):
        cache = {}
        def helper(i, X):
            if i == 1:
                return 1
            key = (i, X)
            if key in cache:
                return cache[key]
            total = 0
            for j in range(len(X)):
                if X[j] % i == 0 or i % X[j] == 0:
                    total += helper(i - 1, X[:j] + X[j + 1:])
            cache[key] = total
            return total
        return helper(N, tuple(range(1, N + 1)))
