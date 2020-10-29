# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 
#
#
# 	'.' Matches any single character.​​​​
# 	'*' Matches zero or more of the preceding element.
#
#
# The matching should cover the entire input string (not partial).
#
#  
# Example 1:
#
#
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#
#
# Example 2:
#
#
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
#
#
# Example 3:
#
#
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
#
#
# Example 4:
#
#
# Input: s = "aab", p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
#
#
# Example 5:
#
#
# Input: s = "mississippi", p = "mis*is*p*."
# Output: false
#
#
#  
# Constraints:
#
#
# 	0 <= s.length <= 20
# 	0 <= p.length <= 30
# 	s contains only lowercase English letters.
# 	p contains only lowercase English letters, '.', and '*'.
# 	It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
#
#


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # if s and not p:
        #     return False
        # if not s:
        #     if p == '.*' or p == '':
        #         return True
        #     else:
        #         return False
            
        pattern = []
        for i in p:
            if i != '*':
                pattern.append(i)
            else:
                pattern[-1] = pattern[-1] + '*'
        dp = [[False] * (len(s)+1) for i in range(len(pattern)+1)]
        dp[0][0] = True
        for i in range(1, len(pattern)+1):
            dp[i][0] = dp[i-1][0] and '*' in pattern[i-1]

        for i in range(1, len(pattern)+1):
            for j in range(1, len(s)+1):
                if '*' not in pattern[i-1] and '.' not in pattern[i-1]:
                    dp[i][j] = dp[i-1][j-1] and pattern[i-1] == s[j-1]
                elif pattern[i-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif '*' in pattern[i-1]:
                    if (dp[i-1][j-1] or dp[i][j-1]) and (pattern[i-1][0] == '.' or pattern[i-1][0] == s[j-1]):
                        dp[i][j] = True
                    elif dp[i-1][j]:
                        dp[i][j] = True
                    # elif dp[i][j-1] and (pattern[i-1][0] == '.' or pattern[i-1][0] == s[j-1]):
                    #     dp[i][j] = True
        return dp[len(pattern)][len(s)]
                    
        
