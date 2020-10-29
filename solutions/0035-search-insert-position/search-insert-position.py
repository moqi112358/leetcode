# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
#  
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4
# Example 4:
# Input: nums = [1,3,5,6], target = 0
# Output: 0
# Example 5:
# Input: nums = [1], target = 0
# Output: 0
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 104
# 	-104 <= nums[i] <= 104
# 	nums contains distinct values sorted in ascending order.
# 	-104 <= target <= 104
#
#


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #  return len([x for x in nums if x<target])
        if target > nums[-1]:
            return len(nums)
        i, j = 0, len(nums)
        while i <= j:
            tmp = int((i+j)/2)
            if nums[tmp] == target:
                return tmp
            elif nums[tmp] > target:
                j = tmp - 1
            elif nums[tmp] < target:
                i = tmp + 1
        return i if target < nums[i]  else i + 1
                
