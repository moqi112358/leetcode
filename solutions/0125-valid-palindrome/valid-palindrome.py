# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid palindrome.
#
# Example 1:
#
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
#
#
# Example 2:
#
#
# Input: "race a car"
# Output: false
#
#


class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=''.join(str for str in s if (str.isalpha() or str.isdigit()))
        return x.lower()==x[::-1].lower()
