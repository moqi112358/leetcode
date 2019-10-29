# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# 	Open brackets must be closed by the same type of brackets.
# 	Open brackets must be closed in the correct order.
#
#
# Note that an empty string is also considered valid.
#
# Example 1:
#
#
# Input: "()"
# Output: true
#
#
# Example 2:
#
#
# Input: "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: "(]"
# Output: false
#
#
# Example 4:
#
#
# Input: "([)]"
# Output: false
#
#
# Example 5:
#
#
# Input: "{[]}"
# Output: true
#
#


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #parenthese = ['(', ')', '{', '}', '[' , ']']
        #tmp = ''.join([i for i in s if i in parenthese])
        '''
        tmp = s
        while '()' in tmp or '[]' in tmp or '{}' in tmp:
            tmp = tmp.replace('()','').replace('[]','').replace('{}','')
        if len(tmp) == 0:
            return True
        else:
            return False
        '''
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
