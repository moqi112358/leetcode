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
        self.res = []
        self.helper(nums, [])
        return self.res

    def helper(self, nums, l):
        if len(nums) == 0:
            self.res.append(l)
            return
        visited = set()
        for i in range(len(nums)):
            if nums[i] not in visited or i == 0:
                self.helper(nums[:i]+nums[i+1:], l + [nums[i]])
            visited.add(nums[i])
