# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
#
#  
# Example 1:
#
#
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#
#
# Example 2:
#
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 8
# 	-10 <= nums[i] <= 10
#
#


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                p = self.permuteUnique(nums[:i] + nums[i+1:])
                for j in p:
                    res.append([nums[i]] + j)
        return res
