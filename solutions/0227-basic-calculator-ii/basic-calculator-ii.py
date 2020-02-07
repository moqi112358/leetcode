# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces  . The integer division should truncate toward zero.
#
# Example 1:
#
#
# Input: "3+2*2"
# Output: 7
#
#
# Example 2:
#
#
# Input: " 3/2 "
# Output: 1
#
# Example 3:
#
#
# Input: " 3+5 / 2 "
# Output: 5
#
#
# Note:
#
#
# 	You may assume that the given expression is always valid.
# 	Do not use the eval built-in library function.
#
#


class Solution:
    # Method 1
#     def calculate(self, s: str) -> int:
#         if not s:
#             return None
#         stack = []
#         l = []
#         i, nums = 0, ''
#         while i < len(s):
#             if s[i] not in '+-*/' and s[i] != ' ':
#                 nums += s[i]
#             elif s[i] == ' ':
#                 i += 1
#                 continue
#             elif s[i] in '+-*/':
#                 l.append(int(nums))
#                 l.append(s[i])
#                 nums = ''
#             i += 1
#         if nums != '':
#             l.append(int(nums))
        
#         i = 0
#         while i < len(l):
#             if l[i] == '+':
#                 i += 1
#             elif l[i] == '-':
#                 stack.append(-1 * l[i+1])
#                 i += 2
#             elif l[i] == '*':
#                 stack[-1] = stack[-1] * l[i+1]
#                 i += 2
#             elif l[i] == '/':
#                 stack[-1] = int(stack[-1] / l[i+1])
#                 i += 2
#             else:
#                 stack.append(l[i])
#                 i += 1
#         return sum(stack)
    def calculate(self, s: str) -> int:
        num,Op,stack = 0,'+',[]
        for i,e in enumerate(s):
            if e.isdigit():
                num = num*10+int(e)
            if e in '+-*/' or i == len(s)-1:
                if Op == '+':
                    stack.append(num)
                if Op == '-':
                    stack.append(-num)
                if Op == '*':
                    stack[-1] = stack[-1] * num
                if Op == '/':
                    stack[-1] = int(stack[-1] / num)
                Op = e
                num = 0
            
                
        return sum(stack)
        
        
        
        
