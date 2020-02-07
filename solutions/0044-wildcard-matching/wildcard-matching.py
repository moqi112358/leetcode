# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
#
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
#
#
# The matching should cover the entire input string (not partial).
#
# Note:
#
#
# 	s could be empty and contains only lowercase letters a-z.
# 	p could be empty and contains only lowercase letters a-z, and characters like ? or *.
#
#
# Example 1:
#
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#
#
# Example 2:
#
#
# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
#
#
# Example 3:
#
#
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
#
#
# Example 4:
#
#
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
#
#
# Example 5:
#
#
# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false
#
#


class Solution:
#     # Method1: Recursion
#     def isMatch(self, s: str, p: str) -> bool:  
#         pattern = ''
#         for i in range(len(p)):
#             if i != 0 and p[i] == '*' and p[i] == p[i-1]:
#                 pass
#             else:
#                 pattern += p[i]
#         print(pattern)
#         return self.helper(s, pattern, 0, 0)
    
#     def helper(self, s, p, index, s_index):
#         # print(s, p, index, s_index)
#         if index == len(p) - 1 and p[index] == '*' and s_index <= len(s):
#             return True
#         if (index >= len(p) and s_index < len(s)) or (index < len(p) and s_index >= len(s)):
#             return False
#         elif index >= len(p) and s_index >= len(s):
#             return True                         
#         if p[index] != '*' and p[index] != '?':
#             if p[index] != s[s_index]:
#                 return False
#             else:
#                 return self.helper(s, p, index+1, s_index+1)
#         elif p[index] == '?':
#             return self.helper(s, p, index+1, s_index+1)
#         elif p[index] == '*':
#             for i in range(s_index, len(s)):
#                 res = self.helper(s, p, index + 1, i)
#                 if res:
#                     return True
    # Method2: DP
    def isMatch(self, s: str, p: str) -> bool:  
        dp = [[False] * (len(s)+1) for i in range(len(p) + 1)]
        dp[0][0] = True
        for i in range(1, len(p)+1):
            dp[i][0] = dp[i-1][0] and p[i-1] == '*'
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] != '*':
                    dp[j][i] = dp[j-1][i-1] and (s[i - 1] == p[j - 1] or p[j - 1] == '?')
                elif p[j-1] == '*':
                    dp[j][i] = dp[j-1][i] or dp[j][i-1] # dp[j-1][i] = True means * == ''
        return dp[len(p)][len(s)]
                    
