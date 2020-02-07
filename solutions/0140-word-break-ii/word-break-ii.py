# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.
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
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
#
#
# Example 2:
#
#
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
#


class Solution:
#     Method1: Backtracking
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: bool
#         """
#         if not wordDict:
#             return []
#         res = []
#         wordDict = set(wordDict)
#         maxLength = max([len(i) for i in wordDict])
#         self.dfs(s, wordDict, maxLength, res, "")
#         return res
        
#     def dfs(self, s, wordDict, maxLength, res, wordpath):
#         if len(s) == 0:
#             print(0)
#             res.append(wordpath.strip())
#             return
#         for i in range(min(maxLength+1, len(s)), 0, -1):
#             # print(s[:i])
#             if s[:i] in wordDict:
#                 # print(s[:i], s[i:], i)
#                 self.dfs(s[i:], wordDict, maxLength, res, wordpath + ' ' + s[:i])
    
    #Method 2
#     def wordBreak(self, s, wordDict):
#         dp = {i: [] for i in range(len(s)+1)}
#         for i in range(len(s)):
#             for word in wordDict:
#                 l = len(word)
#                 if i + 1 >= l and s[i-l+1:i+1] == word:
#                     if i-l+1 == 0:
#                         dp[i+1].append(word)
#                     elif len(dp[i-l+1]) != 0:
#                         for pre_seq in dp[i-l+1]:
#                             dp[i+1].append(pre_seq+' '+word)
#         return dp[len(s)]

    def wordBreak(self, s, wordDict):
        return self.helper(s, wordDict, {})
    
    def helper(self, s, wordDict, dp):
        if s in dp:
            return dp[s]
        if not s:
            return []
        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                tmp = self.helper(s[len(word):], wordDict, dp)
                for seq in tmp:
                    res.append(word + ' ' + seq)
        dp[s] = res
        return dp[s]      
