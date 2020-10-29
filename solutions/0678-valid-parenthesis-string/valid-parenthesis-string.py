#
# Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:
#
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.
#
#
#
# Example 1:
#
# Input: "()"
# Output: True
#
#
#
# Example 2:
#
# Input: "(*)"
# Output: True
#
#
#
# Example 3:
#
# Input: "(*))"
# Output: True
#
#
#
# Note:
#
# The string size will be in the range [1, 100].
#
#


class Solution:
    def checkValidString(self, s: str) -> bool:
        count_star = 0
        count_left = 0
        for i in range(len(s)):
            if s[i] == '(':
                count_left += 1
            elif s[i] == ')':
                count_left -= 1
            elif s[i] == '*':
                count_star += 1
            if count_left >= 0:
                pass
            elif count_left == -1 and count_star > 0:
                count_left += 1
                count_star -= 1
            elif count_left == -1 and count_star == 0:
                return False
        if not (count_left == 0 or count_left <= count_star):
            return False
        
        count_star = 0
        count_left = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                count_left += 1
            elif s[i] == '(':
                count_left -= 1
            elif s[i] == '*':
                count_star += 1
            if count_left >= 0:
                pass
            elif count_left == -1 and count_star > 0:
                count_left += 1
                count_star -= 1
            elif count_left == -1 and count_star == 0:
                return False
        if not (count_left == 0 or count_left <= count_star):
            return False
        
        return True
    
    
    # Stack method
        # stack = []
        # star_stack = []
        # for i in range(len(s)):
        #     if s[i] == '(':
        #         stack.append(i)
        #     elif s[i] == '*':
        #         star_stack.append(i)
        #     else:
        #         if not stack and not star_stack:
        #             return False
        #         if stack:
        #             stack.pop()
        #         else:
        #             star_stack.pop()
        # while stack and star_stack:
        #     if stack.pop()>star_stack.pop():
        #         return False
        # return not stack
        
            
