# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1], k = 3
# Output: true
#
#
#
# Example 2:
#
#
# Input: nums = [1,0,1,1], k = 1
# Output: true
#
#
#
# Example 3:
#
#
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
#
#
#
#
#


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k >= len(nums):
            if len(nums) == len(set(nums)):
                return False
            else:
                return True
        dict = {}
        for i in range(k+1):
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                return True
        for i in range(k+1,len(nums)):
            dict[nums[i-k-1]] -= 1
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                if dict[nums[i]] == 0:
                    dict[nums[i]] = 1
                else:
                    return True
        return False
