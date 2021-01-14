# Given a string, determine if a permutation of the string could form a palindrome.
#
# Example 1:
#
#
# Input: "code"
# Output: false
#
# Example 2:
#
#
# Input: "aab"
# Output: true
#
# Example 3:
#
#
# Input: "carerac"
# Output: true
#


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = collections.Counter(s)
        if len([i for i in counter if counter[i] % 2 == 1]) <= 1:
            return True
        else:
            return False
