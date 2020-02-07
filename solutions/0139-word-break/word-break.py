# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# Note:
#
#
# 	The same word in the dictionary may be reused multiple times in the segmentation.
# 	You may assume the dictionary does not contain duplicate words.
#
#
# Example 1:
#
#
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
#
#
# Example 2:
#
#
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
#
#


class Solution:
    #Method1: Backtracking
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: bool
#         """
#         if not wordDict:
#             return False
#         wordDict = set(wordDict)
#         maxLength = max([len(i) for i in wordDict])
#         return self.dfs(s, wordDict, maxLength)
        
#     def dfs(self, s, wordDict, maxLength):
#         if len(s) == 0:
#             return True
#         for i in range(maxLength+1, 0, -1):
#             # print(s[:i])
#             if s[:i] in wordDict:
#                 res = self.dfs(s[i:], wordDict, maxLength)
#                 if res:
#                     return True
#         return False
    # Method 2: DP
    def wordBreak(self, s, wordDict):
        if not wordDict:
            return False
        dp = [True] + [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                l = len(word)
                if i + 1 >= l and s[i-l+1:i+1] == word and dp[i-l+1]:
                    dp[i+1] = True
                    break
        return dp[-1]
                
                
                
