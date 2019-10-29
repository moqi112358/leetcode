# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
#
# Input: ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Note:
#
# All given inputs are in lowercase letters a-z.
#


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        res = ''
        min_length = min([len(i) for i in strs])
        for i in range(min_length):
            if self.helper(strs, i):
                res += strs[0][i]
            else:
                break
        return res
    def helper(self, strs, i):
        k = ''
        for s in strs:
            if i >= len(s):
                return False
            else:
                if k == '':
                    k = s[i]
                else:
                    if s[i] != k:
                        return False
        return True
    
