# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
#
#  
# Example 1:
#
#
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
#
#
# Example 2:
#
#
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
#
#  
# Constraints:
#
#
# 	n == height.length
# 	0 <= n <= 3 * 104
# 	0 <= height[i] <= 105
#


class Solution:
    # Method1: Color fill
    # def trap(self, height: List[int]) -> int:
    #     if not height:
    #         return 0
    #     matrix = [[0] * len(height) for _ in range(max(height))]
    #     count = len(height) * max(height)
    #     for index in range(len(height)):
    #         for h in range(height[index]):
    #             matrix[h][index] = 1
    #             count -= 1
    #     for h in range(max(height)-1, -1, -1):
    #         if matrix[h][0] == 1:
    #             pass
    #         else:
    #             index = 0
    #             while matrix[h][index] == 0:
    #                 matrix[h][index] = -1
    #                 index += 1
    #                 count -= 1
    #         if matrix[h][len(height)-1] == 1:
    #             pass
    #         else:
    #             index = len(height)-1
    #             while matrix[h][index] == 0:
    #                 matrix[h][index] = -1
    #                 index -= 1
    #                 count -= 1
    #     return count
    
    # Method2 DP
    # def trap(self, height: List[int]) -> int:
    #     left_max, right_max = 0, 0
    #     left_fill, right_fill = 0, 0
    #     count = 0
    #     for i in range(len(height)):
    #         left_max = max(height[i], left_max)
    #         left_fill += left_max
    #         count += height[i]
    #     for i in range(len(height)-1, -1, -1):
    #         right_max = max(height[i], right_max)
    #         right_fill += right_max
    #     return left_fill + right_fill - left_max * len(height) - count
    
    # Method3 Two Pointers
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        res = 0
        while left <= right:
            if left_max <= right_max:
                left_max = max(left_max, height[left])
                res += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                res += right_max - height[right]
                right -= 1
        return res
