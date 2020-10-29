# Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
#
# Input: [2,2,3,2]
# Output: 3
#
#
# Example 2:
#
#
# Input: [0,1,0,1,0,1,99]
# Output: 99
#


class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         s = Counter(nums)
#         for i in s:
#             if s[i] == 1:
#                 return i
    def singleNumber(self, nums: List[int]) -> int:
        return (3 * sum(set(nums)) - sum(nums)) // 2
