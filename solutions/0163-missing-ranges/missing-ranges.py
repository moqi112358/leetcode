# You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.
#
# A number x is considered missing if x is in the range [lower, upper] and x is not in nums.
#
# Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.
#
# Each range [a,b] in the list should be output as:
#
#
# 	"a->b" if a != b
# 	"a" if a == b
#
#
#  
# Example 1:
#
#
# Input: nums = [0,1,3,50,75], lower = 0, upper = 99
# Output: ["2","4->49","51->74","76->99"]
# Explanation: The ranges are:
# [2,2] --> "2"
# [4,49] --> "4->49"
# [51,74] --> "51->74"
# [76,99] --> "76->99"
#
#
# Example 2:
#
#
# Input: nums = [], lower = 1, upper = 1
# Output: ["1"]
# Explanation: The only missing range is [1,1], which becomes "1".
#
#
# Example 3:
#
#
# Input: nums = [], lower = -3, upper = -1
# Output: ["-3->-1"]
# Explanation: The only missing range is [-3,-1], which becomes "-3->-1".
#
#
# Example 4:
#
#
# Input: nums = [-1], lower = -1, upper = -1
# Output: []
# Explanation: There are no missing ranges since there are no missing numbers.
#
#
# Example 5:
#
#
# Input: nums = [-1], lower = -2, upper = -1
# Output: ["-2"]
#
#
#  
# Constraints:
#
#
# 	-109 <= lower <= upper <= 109
# 	0 <= nums.length <= 100
# 	lower <= nums[i] <= upper
# 	All the values of nums are unique.
#
#


class Solution:
    def findMissingRanges(self, A, lower, upper):
        result = []
        A.append(upper+1)
        pre = lower - 1
        for i in A:
            if (i == pre + 2):
                result.append(str(i-1))
            elif (i > pre + 2):
                # print(i, pre+2)
                result.append(str(pre + 1) + "->" + str(i -1))
            pre = i
        return result
    # def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
    #     if not nums:
    #         if upper == lower:
    #             return [str(upper)]
    #         elif upper - lower == 2:
    #             return [str(lower+1)]
    #         else:
    #             return [str(lower+1)+'->'+str(upper)]
    #     res = []
    #     for i in range(len(nums)):
    #         if i == 0 and nums[i] > lower:
    #             res.append(str(lower)+'->'+str(nums[i]-1))
    #         elif  i > upper:
    #             res.append(str(nums[i-1])+'->'+str(upper))
    #             return res
    #         else:
    #             if nums[i] - nums[i-1] <= 1:
    #                 pass
    #             elif nums[i] - nums[i-1] == 2:
    #                 res.append(str(nums[i-1] + 1))
    #             else:
    #                 res.append(str(nums[i-1] + 1)+'->'+str(nums[i]-1))
    #     if nums[-1] < upper:
    #         res.append(str(nums[-1]+1)+'->'+str(upper))
    #     return res
