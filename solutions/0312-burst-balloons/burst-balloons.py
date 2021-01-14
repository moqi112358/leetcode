# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.
#
# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.
#
# Return the maximum coins you can collect by bursting the balloons wisely.
#
#  
# Example 1:
#
#
# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
#
# Example 2:
#
#
# Input: nums = [1,5]
# Output: 10
#
#
#  
# Constraints:
#
#
# 	n == nums.length
# 	1 <= n <= 500
# 	0 <= nums[i] <= 100
#
#


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #dp[i][j] - maxCoin get from all Burst Balloons except balloon i and balloon j
        #rule: dp[i][j] = max(dp[i][k] + dp[k][j] + nums[i] * nums[j] * nums[k]) k = i+1..j-1
        #explain: assume balloom k was the last one burst, since balloon i and j were not included,
        #         so the last score was nums[i] * nums[j] * nums[k], then the problem was divided into 
        #         dp[i][k] and dp[k][j] part (k is not included)
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for i in range(n)]
        for gap in range(2, n):
            for i in range(0, n - gap):
                j = i + gap
                dp[i][j] = max(dp[i][k] + dp[k][j] + nums[i] * nums[j] * nums[k] for k in range(i+1, j))
                
        return dp[0][n-1]

        
