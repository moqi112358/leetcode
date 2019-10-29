# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:
#
# Si % Sj = 0 or Sj % Si = 0.
#
# If there are multiple solutions, return any subset is fine.
#
# Example 1:
#
#
#
# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)
#
#
#
# Example 2:
#
#
# Input: [1,2,4,8]
# Output: [1,2,4,8]
#
#
#


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from copy import copy
        nums.sort()
        n = len(nums)
        if n == 0: return []
        dp = [0] * n
        dp[0] = [nums[0]]
        #print(dp)
        for i in range(1, n):
            curNum = nums[i]
            maxSet = []
            for j in range(i):
                if curNum % nums[j] == 0:
                    localSet = copy(dp[j])
                    if len(localSet) > len(maxSet):
                        maxSet = localSet
            
            maxSet.append(nums[i])
            dp[i] = maxSet
            #print(dp)
        
        #print(dp)
        res = []
        for localSet in dp:
            if len(localSet) > len(res):
                res = localSet
        return res
