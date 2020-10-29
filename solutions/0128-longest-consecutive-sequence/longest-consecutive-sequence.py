# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
# Follow up: Could you implement the O(n) solution? 
#
#  
# Example 1:
#
#
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
#
#
# Example 2:
#
#
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#
#
#  
# Constraints:
#
#
# 	0 <= nums.length <= 104
# 	-109 <= nums[i] <= 109
#
#


class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums = set(nums)
        while nums:
            x = nums.pop()
            l1, l2 = 0, 0
            p, q = x-1, x+1
            while q in nums:
                nums.remove(q)
                q += 1
                l1 += 1
            while p in nums:
                nums.remove(p)
                p -= 1
                l2 += 1
            res = max(res, l1+l2+1)
        return res
            
