# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
#
#  
# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 2 * 104
# 	-1000 <= nums[i] <= 1000
# 	-107 <= k <= 107
#
#


class Solution:
    def subarraySum(self, A, S):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = {0:1}
        cur_sum = 0
        ans = 0
        for i in A:
            cur_sum += i
            if cur_sum - S in count:
                ans += count[cur_sum - S]
            count[cur_sum] = count.get(cur_sum,0) + 1
            
        return ans
        
