# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.
#
# Follow up: Your solution should run in O(log n) time and O(1) space.
#
#  
# Example 1:
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 10^5
# 	0 <= nums[i] <= 10^5
#
#


class Solution:
#     def singleNonDuplicate(self, nums: List[int]) -> int:
#         s = 0
#         for i in range(len(nums)):
#             s += (-1) ** i * nums[i]
#         return s
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid < len(nums) - 1 and nums[mid] == nums[mid + 1]:
                halves_are_even = right - mid - 1
                if halves_are_even % 2 == 1:
                    left = mid + 2
                else:
                    right = mid - 1
            elif mid > 0 and nums[mid] == nums[mid - 1]:
                halves_are_even = right - mid
                if halves_are_even % 2 == 1:
                    left = mid + 1
                else:
                    right = mid - 2
            else:
                return nums[mid]
        return -1
    
    def singleNonDuplicateBruteForce(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0, n - 2, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]
