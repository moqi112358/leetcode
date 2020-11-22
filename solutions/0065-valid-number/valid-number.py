# Validate if a given string can be interpreted as a decimal number.
#
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# " -90e3   " => true
# " 1e" => false
# "e3" => false
# " 6e-1" => true
# " 99e2.5 " => false
# "53.5e93" => true
# " --6 " => false
# "-+3" => false
# "95a54e53" => false
#
# Note: It is intended for the problem statement to be ambiguous. It would be best if you gathered all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:
#
#
# 	Numbers 0-9
# 	Exponent - "e"
# 	Positive/negative sign - "+"/"-"
# 	Decimal point - "."
#
#
# Of course, the context of these characters also matters in the input.
#
#  
# Example 1:
# Input: s = "0"
# Output: true
# Example 2:
# Input: s = "3"
# Output: true
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 20
# 	s consists of only English letters, digits, space ' ', plus '+', minus '-', or dot '.'.
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
