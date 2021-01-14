# Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.
#
# Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.
#
#  
# Example 1:
# Input: n = 12
# Output: 21
# Example 2:
# Input: n = 21
# Output: -1
#
#  
# Constraints:
#
#
# 	1 <= n <= 231 - 1
#
#


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        nums.reverse()
        nums = [int(i) for i in nums]
        stack = deque([])
        flag = 0
        for i in range(len(nums)):
            if len(stack) == 0 or nums[i] >=  stack[-1][1]:
                stack.append((i, nums[i]))
            else:
                flag = 1
                index1 = i
                while stack:
                    if stack[-1][1] > nums[i]:
                        index2 = stack[-1][0]
                        stack.pop()
                    else:
                        break
                break
        if flag == 0:
            return -1
        else:
            nums[index1], nums[index2] = nums[index2], nums[index1]
            nums2 = sorted(nums[:index1], reverse = True)
            for i in range(index1):
                nums[i] = nums2[i]
            nums.reverse()
            nums = [str(i) for i in nums]
            res = int(''.join(nums))
            if res > 2 ** 31 - 1:
                return -1
            return res
