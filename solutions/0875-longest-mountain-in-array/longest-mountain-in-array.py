# You may recall that an array arr is a mountain array if and only if:
#
#
# 	arr.length >= 3
# 	There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
#
# 		arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# 		arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
#
#
#
#
# Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.
#
#  
# Example 1:
#
#
# Input: arr = [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
#
#
# Example 2:
#
#
# Input: arr = [2,2,2]
# Output: 0
# Explanation: There is no mountain.
#
#
#  
# Constraints:
#
#
# 	1 <= arr.length <= 104
# 	0 <= arr[i] <= 104
#
#
#  
# Follow up:
#
#
# 	Can you solve it using only one pass?
# 	Can you solve it in O(1) space?
#
#


# class Solution:
#     def longestMountain(self, A: List[int]) -> int:
#         res = 0
#         cur_max = 0
#         isMountain = 0
#         up_down = 0
#         for i in range(len(A)):
#             if (i != 0 and A[i] <= A[i-1] and isMountain == 0 and up_down != 1) or (i != 0 and A[i] == A[i-1]) or (i != 0 and A[i] > A[i-1] and up_down == -1):
#                 res = max(res, cur_max if isMountain else 0)
#                 if A[i] > A[i-1]:
#                     cur_max = 2
#                     up_down = 1
#                 else:
#                     cur_max = 1
#                     up_down = 0
#                 isMountain = 0
#             elif i == 0:
#                 cur_max += 1
#             elif A[i] > A[i-1]:
#                 up_down = 1
#                 cur_max += 1
#             elif A[i] < A[i-1]:
#                 if (up_down == 1 and isMountain == 0):
#                     isMountain = 1
#                     up_down = -1
#                 elif isMountain == 1:
#                     up_down = -1
#                 cur_max += 1
#             # print(i, res, cur_max, isMountain, up_down)
#         res = max(res, cur_max if isMountain else 0)
#         return res
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A) <= 2:
            return 0
        prev = A[0]
        counter = 0
        max_count = 0
        mode = "asc"
        has_descended = False
        for item in A:
            if item > prev:
                if mode == "asc":
                    counter += 1
                else:
                    max_count = max(max_count, counter)
                    counter = 1
                    mode = "asc"
            elif item < prev:
                if counter >= 1 or mode == "desc":
                    counter += 1
                    mode = "desc"
                    has_descended = True
                else:
                    max_count = max(max_count, counter)
                    counter = 0
            elif item == prev:
                if mode == "desc":
                    max_count = max(max_count, counter)
                    counter = 0
                    mode = "asc"
                else:
                    counter = 0
                    max_count = max(max_count, counter)
            prev = item
        max_count = max(max_count, counter)
        if max_count > 0 and has_descended:
            return max_count + 1
        return 0
