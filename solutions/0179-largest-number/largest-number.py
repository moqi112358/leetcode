# Given a list of non-negative integers nums, arrange them such that they form the largest number.
#
# Note: The result may be very large, so you need to return a string instead of an integer.
#
#  
# Example 1:
#
#
# Input: nums = [10,2]
# Output: "210"
#
#
# Example 2:
#
#
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
#
#
# Example 3:
#
#
# Input: nums = [1]
# Output: "1"
#
#
# Example 4:
#
#
# Input: nums = [10]
# Output: "10"
#
#
#  
# Constraints:
#
#
# 	1 <= nums.length <= 100
# 	0 <= nums[i] <= 109
#
#


class compare(str):
    def __lt__(x, y):
        return x+y > y+x
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s = ''.join(sorted(map(str, nums), key = compare))
        return s if s[0] != '0' else '0'
    
    # mathod 2
#     def largestNumber(self, nums: List[int]) -> str:
#         numsString = [str(num) for num in nums]
#         self.length = len(str(max(nums))) + 1
    
#         def convert(s):
#             num = s
#             while len(num) < self.length:
#                 num += s
#             return int(num[:self.length])
    
#         numsString.sort(key = convert,reverse = True)
#         res = ''.join(numsString)
#         if res[0] == '0':
#             return '0'
#         else:
#             return res
