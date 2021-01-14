# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
#
#  
#
#
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
#
#  
#
#
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
#
#  
#
# Example:
#
#
# Input: [2,1,5,6,2,3]
# Output: 10
#
#
#  
# Example 1:
#
#
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
#
#
# Example 2:
#
#
# Input: heights = [2,4]
# Output: 4
#
#
#  
# Constraints:
#
#
# 	1 <= heights.length <= 105
# 	0 <= heights[i] <= 104
#
#


class Solution:
    # Method 1: Time Out
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         if not heights:
#             return 0
#         res = []
#         for i in range(len(heights)):
#             if not res:
#                 res.append([heights[i], i, i])
#             else:
#                 tmp = [[heights[i], i, i]]
#                 for tmp_res in res:
#                     tmp.append(tmp_res)
#                     if tmp_res[2] + 1 == i:
#                         if heights[i] >= tmp_res[0]:
#                             tmp.append([tmp_res[0], tmp_res[1], i])
#                         else:
#                             tmp.append([heights[i], tmp_res[1], i])
#                 res = tmp
#         res = sorted(res, key = lambda x: x[0] * (x[2] - x[1] + 1), reverse = True)

#         return res[0][0] * (res[0][2] - res[0][1] + 1)

# Method 2: Stack
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        stack = []
        heights.append(0)
        res = 0
        for index, value in enumerate(heights):
            if len(stack) == 0 or value >= stack[-1][1]:
                stack.append((index, value))
            else:
                while len(stack) != 0 and value < stack[-1][1]:
                    pre_index, pre_value = stack.pop()
                    res = max(res, (index - pre_index) * pre_value)
                stack.append((pre_index, value))
        return res
                    
        
