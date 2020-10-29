# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
#
# Each letter in the magazine string can only be used once in your ransom note.
#
#  
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
#
#  
# Constraints:
#
#
# 	You may assume that both strings contain only lowercase letters.
#
#


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        ransom_counter = Counter(ransomNote)
        mag_counter = Counter(magazine)
        for i in ransom_counter:
            if i not in mag_counter or ransom_counter[i] > mag_counter[i]:
                return False
        return True
