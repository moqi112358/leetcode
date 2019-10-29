# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
#
# Example 1:
#
#
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#
# Example 2:
#
#
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
#              jump length is 0, which makes it impossible to reach the last index.
#
#


class Solution:
    def canJump(self, nums):
        '''
        if len(nums) <= 1:
            return True
        res = [0] * len(nums)
        res[0] = 1
        for i in range(len(nums)):
            if res[i] == 0:
                return False
            else:
                for j in range(1, nums[i]+1):
                    if i + j >= len(res) - 1:
                        return True
                    else:
                        res[i+j] = 1
        '''
        # if nums[i] can be reached, then nums[i-1] can be reached too
        goal = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
        return not goal
        
