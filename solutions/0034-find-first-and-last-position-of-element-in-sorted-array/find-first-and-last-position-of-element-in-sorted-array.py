# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# Follow up: Could you write an algorithm with O(log n) runtime complexity?
#
#  
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
#
#  
# Constraints:
#
#
# 	0 <= nums.length <= 105
# 	-109 <= nums[i] <= 109
# 	nums is a non-decreasing array.
# 	-109 <= target <= 109
#
#


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        start, end = -1, -1
        while l < r:
            mid = int((l + r) / 2)
            if nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] == target:
                mid_s, mid_e = mid, mid
                if mid_s == 0 or nums[mid_s] > nums[mid_s - 1]:
                    start = mid_s
                else:
                    while l < mid_s:
                        start = int((l + mid_s) / 2)
                        if nums[start] < target:
                            l = start + 1
                        elif nums[start] == target:
                            if start == 0:
                                break
                            elif nums[start - 1] < target:
                                break
                            elif nums[start - 1] == target:
                                mid_s = start
                if mid_e == len(nums) - 1 or nums[mid_s] > nums[mid_s + 1]:
                    end = mid_e
                else:
                    while mid_e < r:
                        end = int((r + mid_e) / 2)
                        if nums[end] > target:
                            r = end
                        elif nums[end] == target:
                            if end == len(nums) - 1:
                                break
                            elif nums[end + 1] > target:
                                break
                            elif nums[end + 1] == target:
                                mid_e = end + 1
                if mid_e == r:
                    end = mid_e
                if mid_s == l:
                    start = mid_s
                return [start, end]
        if l == r and nums[l] == target:
            return [l, r]
        return [start, end]
        
