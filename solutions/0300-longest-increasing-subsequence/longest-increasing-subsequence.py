# Given an unsorted array of integers, find the length of longest increasing subsequence.
#
# Example:
#
#
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
#
# Note: 
#
#
# 	There may be more than one LIS combination, it is only necessary for you to return the length.
# 	Your algorithm should run in O(n2) complexity.
#
#
# Follow up: Could you improve it to O(n log n) time complexity?
#


class Solution:
    # Brute Force
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     return self.findLength(nums, min(nums) - 1, 0)
    # def findLength(self, nums, prev, index):
    #     if index == len(nums):
    #         return 0
    #     taken = 0
    #     if nums[index] > prev:
    #         taken = 1 + self.findLength(nums, nums[index], index+1)
    #     untaken = self.findLength(nums, prev, index+1)
    #     return max(taken, untaken)
                
        
    # # DP
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     if not nums: return 0 
    #     dp = [1] * len(nums)
    #     for i in range(len(nums)):
    #         for j in range(0, i):
    #             if nums[j] < nums[i] and dp[i] < dp[j] + 1:
    #                 dp[i] = dp[j] + 1
    #     return max(dp)
    
    # nlgn
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        B = []
        B.append(nums[0])
        for i in range(1, len(nums)):
            B = self.insertB(B, nums[i])
        print(B)
        return len(B)
    
    def insertB(self, B, nums):
        if nums < B[0]:
            B[0] = nums
        elif nums > B[-1]:
            B.append(nums)
        else:
            i, j = 0, len(B) - 1
            while i < j:
                mid = int((i+j)/2)
                if B[mid] == nums:
                    return B
                elif B[mid] > nums:
                    j = mid
                elif B[mid] < nums:
                    i = mid + 1
            if B[i-1] < nums < B[i]:
                B[i] = nums
            elif B[i] < nums < B[i+1]:
                B[i+1] = nums
        return B
