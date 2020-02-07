# Given a list of non negative integers, arrange them such that they form the largest number.
#
# Example 1:
#
#
# Input: [10,2]
# Output: "210"
#
# Example 2:
#
#
# Input: [3,30,34,5,9]
# Output: "9534330"
#
#
# Note: The result may be very large, so you need to return a string instead of an integer.
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
