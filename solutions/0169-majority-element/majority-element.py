# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
#
#  
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
#  
# Constraints:
#
#
# 	n == nums.length
# 	1 <= n <= 5 * 104
# 	-231 <= nums[i] <= 231 - 1
#
#
#  
# Follow-up: Could you solve the problem in linear time and in O(1) space?


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        ele = None
        for i in nums:
            if count == 0:
                count = 1
                ele = i
            elif ele == i:
                count += 1
            elif ele != i:
                count -= 1
        return ele
        
