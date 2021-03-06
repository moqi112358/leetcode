# Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".
#
# Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.
#
#  
# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
#
#  
# Constraints:
#
#
# 	1 <= s.length, t.length <= 105
# 	s and t consist of English letters.
#
#
#  
# Follow up: Could you find an algorithm that runs in O(n) time?


class Solution:
#     Method1:
#     def minWindow(self, s: str, t: str) -> str:
#         from collections import Counter
#         q = []
#         res_len = float('inf')
#         res = ''
#         count_t = Counter(t)
#         count_c = {}
#         i, j = 0, 0
        
#         while j < len(s):
#             count_c[s[j]] = count_c.get(s[j],0) + 1
#             if self.checkContain(count_t, count_c):
#                 while s[i] not in count_t or count_c[s[i]] > count_t[s[i]]:
#                     count_c[s[i]] -= 1
#                     i += 1
#                 if j - i + 1 <= res_len:
#                     res_len = j - i + 1
#                     res = s[i:j+1]
#                 count_c[s[i]] -= 1
#                 i += 1
#             j += 1
#         return res
            

#     def checkContain(self, count_t, count_c):
#         for k in count_t:
#             if k not in count_c:
#                 return False
#             if count_c[k] < count_t[k]:
#                 return False
#         return True

    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        q = []
        res_len = float('inf')
        res = ''
        count_t = Counter(t)
        count_c = {}
        i, j = 0, 0
        missing = ''
        len_k = 0
        while j < len(s):
            count_c[s[j]] = count_c.get(s[j],0) + 1
            if s[j] in count_t and count_c[s[j]] <= count_t[s[j]]:
                len_k += 1
            while len_k == len(t):
                if j - i + 1 <= res_len:
                    res_len = j - i + 1
                    res = s[i:j+1]
                if s[i] not in count_t or count_c[s[i]] > count_t[s[i]]:
                    count_c[s[i]] -= 1
                    i += 1
                elif s[i] in count_t and count_c[s[i]] == count_t[s[i]]:
                    count_c[s[i]] -= 1
                    i += 1
                    len_k -= 1
            j += 1
        return res
                
