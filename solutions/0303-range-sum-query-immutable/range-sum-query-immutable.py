# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
#
# Implement the NumArray class:
#
#
# 	NumArray(int[] nums) Initializes the object with the integer array nums.
# 	int sumRange(int i, int j) Return the sum of the elements of the nums array in the range [i, j] inclusive (i.e., sum(nums[i], nums[i + 1], ... , nums[j]))
#
#
#  
# Example 1:
#
#
# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]
#
# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
# numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1)) 
# numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
#
#
#  
# Constraints:
#
#
# 	0 <= nums.length <= 104
# 	-105 <= nums[i] <= 105
# 	0 <= i <= j < nums.length
# 	At most 104 calls will be made to sumRange.
#
#


class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = [0] * len(nums)
        for i in range(len(nums)):
            self.dp[i] = nums[i] + self.dp[i-1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j] - (self.dp[i-1] if i > 0 else 0)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
