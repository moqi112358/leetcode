# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#
#
# Example 2:
#
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
#


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        pivot_index = max(0, self.binarySearch(nums, target, True))
        if pivot_index == 0:
            pivot_index = len(nums)
        if target >= nums[0]:
            return self.binarySearch(nums[:pivot_index], target, False)
        else:
            res = self.binarySearch(nums[pivot_index:], target, False)
            if res == -1:
                return res
            else:
                return pivot_index + res
        
    def binarySearch(self, nums, target, findpivot):
        l, r = 0, len(nums) - 1
        if findpivot:
            while l <= r:
                mid = int((l + r) / 2)
                if mid == len(nums) - 1:
                    return 0
                elif nums[mid] >= nums[mid+1]:
                    return mid + 1
                elif nums[mid] >= nums[0]:
                    l = mid + 1
                elif nums[mid] < nums[0]:
                    r = mid - 1
        else:
            if len(nums) == 0:
                return -1
            while l < r:
                mid = int((l + r) / 2)
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid
                elif nums[mid] < target:
                    l = mid + 1
            if nums[r] == target:
                return r
            else:
                return -1
