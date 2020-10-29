# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
#
#  
# Example 1:
#
#
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
#
#
# Example 3:
#
#
# Input: nums = [0]
# Output: 0
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 100
# 	0 <= nums[i] <= 1000
#
#


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.dpAlgorithm(nums[1:]), self.dpAlgorithm(nums[:len(nums)-1]))
    def dpAlgorithm(self, nums):
        dp = [[0] * 2 for _ in nums]
        # dp[i][0] - not rob
        # dp[i][1] - rob
        dp[0][1] = nums[0]
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0] + nums[i]
        return max(dp[-1][0], dp[-1][1])
