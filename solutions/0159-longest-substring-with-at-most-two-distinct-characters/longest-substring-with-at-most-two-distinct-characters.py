# Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.
#
# Example 1:
#
#
# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.
#
#
# Example 2:
#
#
# Input: "ccaabbb"
# Output: 5
# Explanation: t is "aabbb" which its length is 5.
#
#


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        alphabet = set()
        start, cur = 0, 0
        res = 0
        while cur < len(s):
            if s[cur] in alphabet:
                cur += 1
            elif s[cur] not in alphabet and len(alphabet) < 2:
                alphabet.add(s[cur])
                cur += 1
            elif s[cur] not in alphabet and len(alphabet) == 2:
                res = max(res, cur - start)
                start, keep = cur - 1, s[cur-1]
                while start > 0 and s[start] == keep:
                    start -= 1
                start += 1
                alphabet.remove(s[start - 1])
                alphabet.add(s[cur])
                cur += 1
        res = max(res, cur - start)
        return res
                
