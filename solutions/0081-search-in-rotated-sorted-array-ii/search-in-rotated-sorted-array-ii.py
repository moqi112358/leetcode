# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
#
# You are given a target value to search. If found in the array return true, otherwise return false.
#
# Example 1:
#
#
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
#
#
# Example 2:
#
#
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
#
# Follow up:
#
#
# 	This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
# 	Would this affect the run-time complexity? How and why?
#
#


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Initilize two pointers
        begin = 0
        end = len(nums) - 1 
        while begin <= end:
            mid = (begin + end)//2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[end]: # Fail to estimate which side is sorted
                end -= 1  # In worst case: O(n)
            elif nums[mid] > nums[end]: # Left side of mid is sorted
                if  nums[begin] <= target and target < nums[mid]: # Target in the left side
                    end = mid - 1
                else: # in right side
                    begin = mid + 1
            else: # Right side is sorted
                if  nums[mid] < target and target <= nums[end]: # Target in the right side
                    begin = mid + 1
                else: # in left side
                    end = mid - 1
        return False
