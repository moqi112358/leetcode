# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
#
#  
#
# Example 1:
#
#
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
#
#
# Example 2:
#
#
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
#
#
#  
# Constraints:
#
#
# 	The input strings only contain lower case letters.
# 	The length of both given strings is in range [1, 10,000].
#
#


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hash_s1 = {chr(i):0 for i in range(97,123)}
        hash_s2 = {chr(i):0 for i in range(97,123)}
        for i in range(len(s1)):
            hash_s1[s1[i]] += 1
            hash_s2[s2[i]] += 1
        len_s1 = len(s1)
        for i in range(len_s1, len(s2)):
            if hash_s1 == hash_s2:
                return True
            hash_s2[s2[i]] += 1
            hash_s2[s2[i-len_s1]] = max(0, hash_s2[s2[i-len_s1]] - 1)
        if hash_s1 == hash_s2:
            return True
        return False
        
