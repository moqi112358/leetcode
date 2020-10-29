# Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
#
# Return true if there is a 132 pattern in nums, otherwise, return false.
#
# Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?
#
#  
# Example 1:
#
#
# Input: nums = [1,2,3,4]
# Output: false
# Explanation: There is no 132 pattern in the sequence.
#
#
# Example 2:
#
#
# Input: nums = [3,1,4,2]
# Output: true
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
#
#
# Example 3:
#
#
# Input: nums = [-1,3,2,0]
# Output: true
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
#
#
#  
# Constraints:
#
#
# 	n == nums.length
# 	1 <= n <= 104
# 	-109 <= nums[i] <= 109
#
#


class Solution:
    # def find132pattern(self, nums: List[int]) -> bool:
    #     m_list = []
    #     m = float('inf')
    #     for i in nums:
    #         m = min(m, i)
    #         m_list.append(m)
    #     stack = []
    #     for i in range(len(nums)-1, -1, -1):
    #         if len(stack) == 0:
    #             if nums[i] > m_list[i]:
    #                 stack.append(nums[i])
    #         else: #  nums[i] >= m_list[i]
    #             if nums[i] == m_list[i]:
    #                 continue
    #             elif nums[i] > stack[-1] and stack[-1] > m_list[i]:
    #                 return True
    #             elif nums[i] < stack[-1] and stack[-1] > m_list[i]:
    #                 stack.append(nums[i])
    #             elif stack[-1] <= m_list[i]:
    #                 while len(stack) > 0 and m_list[i] >= stack[-1]:
    #                     stack.pop()
    #                 if len(stack) > 0:
    #                     return True
    #                 else:
    #                     stack.append(nums[i])
    #     return False
     def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        third = float('-inf')
        for n in nums[::-1]:
            if n < third:
                return True
            while stack and stack[-1] < n:
                third = stack.pop()
            stack.append(n)
        return False
