# Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.
#
#  
# Example 1:
#
#
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: The substring is "ece" with length 3.
#
# Example 2:
#
#
# Input: s = "aa", k = 1
# Output: 2
# Explanation: The substring is "aa" with length 2.
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 5 * 104
# 	0 <= k <= 50
#
#


from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if n * k == 0:
            return 0

        # sliding window left and right pointers
        left, right = 0, 0
        # hashmap character -> its rightmost position
        # in the sliding window
        hashmap = defaultdict()

        max_len = 1

        while right < n:
            # add new character and move right pointer
            hashmap[s[right]] = right
            right += 1

            if len(hashmap) == k + 1:
                # delete the leftmost character
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                # move left pointer of the slidewindow
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len
