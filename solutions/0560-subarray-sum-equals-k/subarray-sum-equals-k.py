# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
#
# Example 1:
#
# Input:nums = [1,1,1], k = 2
# Output: 2
#
#
#
# Note:
#
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
#
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
        
