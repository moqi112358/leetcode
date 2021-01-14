# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
#
#  
# Example 1:
# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:
# Input: nums = [0,1,0,1,0,1,99]
# Output: 99
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 3 * 104
# 	-231 <= nums[i] <= 231 - 1
# 	Each element in nums appears exactly three times except for one element which appears once.
#
#
#  
# Follow up: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#


class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         s = Counter(nums)
#         for i in s:
#             if s[i] == 1:
#                 return i
    def singleNumber(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2
