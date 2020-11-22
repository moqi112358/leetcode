# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
#
#  
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 6
# 	-10 <= nums[i] <= 10
# 	All the integers of nums are unique.
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
