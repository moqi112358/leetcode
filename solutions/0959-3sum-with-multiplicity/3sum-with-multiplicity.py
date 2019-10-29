# -*- coding:utf-8 -*-


# Given an integer array A, and an integer target, return the number of tuples i, j, k  such that i < j < k and A[i] + A[j] + A[k] == target.
#
# As the answer can be very large, return it modulo 10^9 + 7.
#
#  
#
# Example 1:
#
#
# Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
# Output: 20
# Explanation: 
# Enumerating by the values (A[i], A[j], A[k]):
# (1, 2, 5) occurs 8 times;
# (1, 3, 4) occurs 8 times;
# (2, 2, 4) occurs 2 times;
# (2, 3, 3) occurs 2 times.
#
#
#
# Example 2:
#
#
# Input: A = [1,1,2,2,2,2], target = 5
# Output: 12
# Explanation: 
# A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
# We choose one 1 from [1,1] in 2 ways,
# and two 2s from [2,2,2,2] in 6 ways.
#
#
#  
#
#
# Note:
#
#
# 	3 <= A.length <= 3000
# 	0 <= A[i] <= 100
# 	0 <= target <= 300
#


class Solution(object):
    def threeSumMulti(self, nums, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        import operator
        nums.sort()
        results = []
        length = len(nums)
        for i in range(0, length - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            tmp = target - nums[i]
            left, right = i + 1, length - 1
            while left < right:
                if nums[left] + nums[right] == tmp:
                    results.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                          left += 1
                    while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                elif nums[left] + nums[right] > tmp:
                    right -= 1
                else:
                    left += 1
        total_count = {}
        for i in set(nums):
            total_count[i] = nums.count(i)
        res = 0
        for r in results:
            tmp = 1
            for k in set(r):
                tmp *= self.c(total_count[k],r.count(k))
            res += tmp
        return res % (10**9 + 7)
    
    def c(self,n,k):
        return  reduce(operator.mul, range(n - k + 1, n + 1)) /reduce(operator.mul, range(1, k +1))
            
