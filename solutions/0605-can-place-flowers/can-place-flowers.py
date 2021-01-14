# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
#
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.
#
#  
# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
#
#  
# Constraints:
#
#
# 	1 <= flowerbed.length <= 2 * 104
# 	flowerbed[i] is 0 or 1.
# 	There are no two adjacent flowers in flowerbed.
# 	0 <= n <= flowerbed.length
#
#


# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         candidate = []
#         for i in range(len(flowerbed)):
#             if flowerbed[i] == 1:
#                 continue
#             if i - 1 >= 0 and flowerbed[i - 1] == 1:
#                 continue
#             if i + 1 < len(flowerbed) and flowerbed[i + 1] == 1:
#                 continue
#             candidate.append(i)
#         if len(candidate) == 0 and n > 0:
#             return False
#         elif len(candidate) == 0 and n == 0:
#             return True
#         dp = [[-1, -1] for _ in candidate] # 0 - use 1 - not use
#         dp[0][0] = 1
#         for i in range(1, len(candidate)):
#             if candidate[i] - candidate[i-1] > 1:
#                 dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + 1
#                 dp[i][1] = max(dp[i-1][0], dp[i-1][1])
#             elif candidate[i] - candidate[i-1] == 1:
#                 dp[i][0] = dp[i-1][1] + 1
#                 dp[i][1] = max(dp[i-1][0], dp[i-1][1])
#         return n <= max(dp[-1][0], dp[-1][1])
class Solution:
    def canPlaceFlowers(self, A, n):
        x = 0
        A = [0] + A + [0]
        for i in range(1, len(A)-1):
            if A[i]==1:
                continue   
            if not A[i-1]+A[i+1]:
                A[i] = 1
                x += 1
        return x>=n
        
        
