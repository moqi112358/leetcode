# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
#
#
# 	"123"
# 	"132"
# 	"213"
# 	"231"
# 	"312"
# 	"321"
#
#
# Given n and k, return the kth permutation sequence.
#
#  
# Example 1:
# Input: n = 3, k = 3
# Output: "213"
# Example 2:
# Input: n = 4, k = 9
# Output: "2314"
# Example 3:
# Input: n = 3, k = 1
# Output: "123"
#
#  
# Constraints:
#
#
# 	1 <= n <= 9
# 	1 <= k <= n!
#
#


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = ""
        visited = [0] * n
        rest = n
        while len(res) != n:
            if rest == 1:
                res += str([i+1 for i in range(len(visited)) if visited[i] == 0][0] )
                continue
            m = self.helper(rest - 1)
            p = (k-1) // m
            num = [i+1 for i in range(len(visited)) if visited[i] == 0][p] 
            visited[num-1] = 1
            res += str(num)
            k -= m * p
            rest -= 1
        return res
    
    def helper(self, n):
        k = 1
        for i in range(1, n+1):
            k *= i
        return k
