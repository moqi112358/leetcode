# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#
#


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        S = set(nums)
        l = []
        self.res = []
        self.helper(l, S)
        return self.res

    def helper(self, l, S):
        if len(S) == 0:
            res_l = l.copy()
            self.res.append(res_l)
        for i in S:
            tmp_S, tmp_l = S.copy(), l.copy()
            tmp_S.remove(i)
            tmp_l.append(i)
            self.helper(tmp_l, tmp_S)
