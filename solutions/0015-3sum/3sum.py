# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                hres = self.helper(-1 * nums[i], nums[i+1:])
                for r in hres:
                    tmp = r + [nums[i]]
                    res.append(tmp)
        return res

    def helper(self, target, array):
        h = {}
        res = []
        for i in range(len(array)):
            if target - array[i] in h and h[target - array[i]] == 1:
                res.append([array[i], target - array[i]])
                h[target - array[i]] = 0
                h[array[i]] = 0
            if array[i] in h:
                pass
            else:
                h[array[i]] = 1
        return res
