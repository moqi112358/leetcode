# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# You can assume that you can always reach the last index.
#
#  
# Example 1:
#
#
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#
# Example 2:
#
#
# Input: nums = [2,3,0,1,4]
# Output: 2
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 3 * 104
# 	0 <= nums[i] <= 105
#
#


class Solution:
    # method 1
    # def jump(self, nums: List[int]) -> int:
    #     res = [len(nums) + 1] * len(nums)
    #     res[0] = 0
    #     for i in range(len(nums)):
    #         if res[i] != len(nums) + 1:
    #             for j in range(1, nums[i] + 1):
    #                 if i + j < len(nums):
    #                     res[i + j] = min(res[i + j], res[i] + 1)
    #     if res[-1] == len(nums) + 1:
    #         return -1
    #     return res[-1]
    # method 2
    #     def jump(self, nums: List[int]) -> int:
    #         self.res = [len(nums) + 1] * len(nums)
    #         self.res[-1] = 0
    #         self.helper(nums, len(nums) - 1)
    #         return self.res[0]
    
    #     def helper(self, nums, index):
    #         for i in range(index - 1, -1, -1):
    #             if i + nums[i] >= index:
    #                 self.res[i] = min(self.res[i], self.res[index] + 1)
    #                 self.helper(nums, i)
    #             else:
    #                 pass
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return 1
        if len(nums) == 1:
            return 0
        l, r = 0, nums[0]
        times = 1
        while r < len(nums) - 1:
            nxt = max([ i + nums[i] for i in range(l, r+1)])
            times += 1
            l, r = r + 1, nxt
        return times
