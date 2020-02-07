# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
#
# Example:
#
#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
#
#
# Note:
#
#
# 	If there is no such window in S that covers all characters in T, return the empty string "".
# 	If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
#
#


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
                
