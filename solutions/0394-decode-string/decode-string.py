# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
#
#  
# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
# Example 4:
# Input: s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 30
# 	s consists of lowercase English letters, digits, and square brackets '[]'.
# 	s is guaranteed to be a valid input.
# 	All the integers in s are in the range [1, 300].
#
#


class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        i = 0
        while i < len(s):
            if not s[i].isdigit():
                res += s[i]
                i += 1
                continue
            else:
                repeattimes = ''
                while s[i] != '[':
                    repeattimes += s[i]
                    i += 1
                repeattimes = int(repeattimes)
                countBrackets = 1
                i += 1
                pattern = ''
                while True:
                    if s[i] == '[':
                        countBrackets += 1
                    elif s[i] == ']':
                        countBrackets -= 1               
                    if countBrackets == 0:
                        i += 1
                        break
                    else:
                        pattern += s[i]
                        i += 1
                decodepatter = self.decodeString(pattern)
                res += repeattimes * decodepatter
        return res
