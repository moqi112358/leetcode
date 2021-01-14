# Given a string s which represents an expression, evaluate this expression and return its value. 
#
# The integer division should truncate toward zero.
#
#  
# Example 1:
# Input: s = "3+2*2"
# Output: 7
# Example 2:
# Input: s = " 3/2 "
# Output: 1
# Example 3:
# Input: s = " 3+5 / 2 "
# Output: 5
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 3 * 105
# 	s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
# 	s represents a valid expression.
# 	All the integers in the expression are non-negative integers in the range [0, 231 - 1].
# 	The answer is guaranteed to fit in a 32-bit integer.
#
#


# class Solution:
#     def calculate(self, s: str) -> int:
#         stack = []
#         calfirst = 0
#         num = ''
#         s = ''.join([i for i in s if i != ' '])
#         s += '+0'
#         for i in s:
#             if i in [str(i) for i in range(0, 10)]:
#                 num += i
#                 continue
#             if i == '*' or i == '/' or i == '+' or i == '-':
#                 if calfirst == 0:
#                     stack.append(int(num))
#                     num = ''
#                     stack.append(i)
#                 else:
#                     sign = stack.pop()
#                     last_num = stack.pop()
#                     if sign == '*':
#                         stack.append(int(num) * last_num)
#                     elif sign == '/':
#                         stack.append(last_num // int(num))
#                     stack.append(i)
#                     num = ''
#                 if i == '+' or i == '-':
#                     calfirst = 0
#                 else:
#                     calfirst = 1
#         res = 0
#         sign = '+'
#         for i in stack:
#             if i != '+' and i != '-':
#                 if sign == '+':
#                     res += i
#                 else:
#                     res -= i
#             if i == '+':
#                 sign = '+'
#             if i == '-':
#                 sign = '-'
#         return res
class Solution:
    def calculate(self, s: str) -> int:
        val = 0
        stack = []
        op = '+'        
        for c in s+'+':
            if c.isdigit():
                val = val*10+ int(c)
            elif c in '+-*/':
                if op == '+':
                    stack.append(val)
                elif op == '-':
                    stack.append(-val)
                elif op == '*':
                    stack[-1] = stack[-1]*val
                elif op == '/':
                    stack[-1] = int(stack[-1]/val)
                op = c
                val = 0
        return sum(stack)
