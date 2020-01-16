# Given an unsorted integer array, find the smallest missing positive integer.
#
# Example 1:
#
#
# Input: [1,2,0]
# Output: 3
#
#
# Example 2:
#
#
# Input: [3,4,-1,1]
# Output: 2
#
#
# Example 3:
#
#
# Input: [7,8,9,11,12]
# Output: 1
#
#
# Note:
#
# Your algorithm should run in O(n) time and uses constant extra space.
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
    
