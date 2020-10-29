# Given an unsorted integer array nums, find the smallest missing positive integer.
#
# Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space.?
#
#  
# Example 1:
# Input: nums = [1,2,0]
# Output: 3
# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1
#
#  
# Constraints:
#
#
# 	0 <= nums.length <= 300
# 	-231 <= nums[i] <= 231 - 1
#
#


class Solution:
    # #O(n) time and O(n) space
    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     if not nums or max(nums) <= 0:
    #         return 1
    #     smallest = min([i for i in nums if i > 0])
    #     if smallest != 1:
    #         return 1
    #     s = set(nums)
    #     while True:
    #         if smallest in s:
    #             smallest += 1
    #         else:
    #             return  smallest
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums or max(nums) <= 0:
            return 1
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] >= n or nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            nums[nums[i]%n] += n
        print(nums)
        for i in range(len(nums)):
            if nums[i] // n == 0:
                return i
        return len(nums)
    
