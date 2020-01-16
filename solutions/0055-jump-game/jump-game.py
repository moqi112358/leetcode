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
    def canJump(self, nums: List[int]) -> bool:
        #method 1
        # res = [False] * len(nums)
        # res[0] = True
        # for i in range(len(nums)):
        #     if res[i] is False:
        #         return False
        #     else:
        #         for j in range(nums[i] + 1):
        #             if i + j < len(res):
        #                 res[i + j] = True
        # return res[-1]
        #method 2
        if len(nums) == 1:
            return True
        last_ind = len(nums) - 1
        while True:
            flag = 0
            for i in range(last_ind - 1, -1, -1):
                if nums[i] + i >= last_ind:
                    last_ind = i
                    flag = 1
                    break
            if last_ind == 0:
                return True
            elif flag == 0:
                return False
        # method 3
        # if nums[i] can be reached, then nums[i-1] can be reached too
        # goal = len(nums) - 1
        # for i in range(len(nums))[::-1]:
        #     if i + nums[i] >= goal:
        #         goal = i
        # return not goal  

    

        
