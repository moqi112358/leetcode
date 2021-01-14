# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
#
#
#  
# Example 1:
#
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
#
# Example 2:
#
#
# Input: digits = ""
# Output: []
#
#
# Example 3:
#
#
# Input: digits = "2"
# Output: ["a","b","c"]
#
#
#  
# Constraints:
#
#
# 	0 <= digits.length <= 4
# 	digits[i] is a digit in the range ['2', '9'].
#


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {'2': ['a','b','c'],
                     '3': ['d','e','f'],
                     '4': ['g','h','i'],
                     '5': ['j','k','l'],
                     '6': ['m','n','o'],
                     '7': ['p','q','r','s'],
                     '8': ['t','u','v'],
                     '9': ['w','x','y','z']
                    }
        res = []
        if len(digits) == 0:
            return res
        self.helper(digit_map, digits, 0, '', res)
        return res
    
    def helper(self, digit_map, digits, index, s, res):
        if index == len(digits):
            res.append(s)
            return
        for i in range(len(digit_map[digits[index]])):
            self.helper(digit_map, digits, index + 1, s + digit_map[digits[index]][i], res)
        
