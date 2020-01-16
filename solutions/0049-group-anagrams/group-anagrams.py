# Given an array of strings, group anagrams together.
#
# Example:
#
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
#
# Note:
#
#
# 	All inputs will be in lowercase.
# 	The order of your output does not matter.
#
#


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_word = {}
        for i in strs:
            tmp = ''.join(sorted(i))
            if tmp in hash_word:
                hash_word[tmp].append(i)
            else:
                hash_word[tmp] = [i]
        return list(hash_word.values())
