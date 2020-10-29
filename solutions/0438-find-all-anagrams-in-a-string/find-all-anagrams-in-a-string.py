# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
#
#
# Example 2:
#
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#
#


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p or len(s) < len(p):
            return []
        from collections import Counter
        len_p = len(p)
        counter_p = Counter(p)
        counter_s = Counter(s[:len_p])
        for i in counter_s:
            if i not in counter_p:
                counter_p[i] = 0
        res = []
        for i in range(len_p, len(s)):
            if counter_s == counter_p:
                res.append(i - len_p)
            counter_s[s[i - len_p]] -= 1
            counter_s[s[i]] += 1
            if s[i] not in counter_p:
                counter_p[s[i]] = 0
        if counter_s == counter_p:
            res.append(len(s) - len_p)
        return res
        
        
