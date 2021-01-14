# A valid number can be split up into these components (in order):
#
#
# 	A decimal number or an integer.
# 	(Optional) An 'e' or 'E', followed by an integer.
#
#
# A decimal number can be split up into these components (in order):
#
#
# 	(Optional) A sign character (either '+' or '-').
# 	One of the following formats:
#
# 		At least one digit, followed by a dot '.'.
# 		At least one digit, followed by a dot '.', followed by at least one digit.
# 		A dot '.', followed by at least one digit.
#
#
#
#
# An integer can be split up into these components (in order):
#
#
# 	(Optional) A sign character (either '+' or '-').
# 	At least one digit.
#
#
# For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].
#
# Given a string s, return true if s is a valid number.
#
#  
# Example 1:
#
#
# Input: s = "0"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "e"
# Output: false
#
#
# Example 3:
#
#
# Input: s = "."
# Output: false
#
#
# Example 4:
#
#
# Input: s = ".1"
# Output: true
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 20
# 	s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
#
#


class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # check Exponent 
        if 'e' in s:
            if s.count('e') > 1:
                return False
            index = s.index('e')
            if index == 0 or index == len(s) - 1:
                return False
            tag1 = self.isNumber(s[0:index])
            tag2 = self.isNumber(s[index+1:len(s)])
            tag3 = s[index+1] != ' ' and s[index-1] != ' '
            tag4 = '.' not in s[index+1:len(s)]
            return tag1 and tag2 and tag3 and tag4 
        else:
            tmp = s.strip()
            # check none e.g 'e3'
            if len(tmp) == 0 or s is None:
                return False
            # check sign 
            if (tmp[0] == '+' or tmp[0] == '-'):
                tmp = tmp[1:len(s)]
            # check number
            flag = 0
            for i in tmp:
                if not i.isdigit() and i != '.':
                    return False
                elif i.isdigit():
                    flag = 1
            # check no number
            if flag == 0:
                return False
            if tmp.count('.') > 1:
                return False
        return True
