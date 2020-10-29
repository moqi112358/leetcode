# Given an array of characters chars, compress it using the following algorithm:
#
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
#
#
# 	If the group's length is 1, append the character to s.
# 	Otherwise, append the character followed by the group's length.
#
#
# The compressed string s should not be returned separately, but instead be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
#
# After you are done modifying the input array, return the new length of the array.
#  
#
# Follow up:
# Could you solve it using only O(1) extra space?
#
#  
# Example 1:
#
#
# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
#
#
# Example 2:
#
#
# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a single character.
#
#
# Example 3:
#
#
# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
#
# Example 4:
#
#
# Input: chars = ["a","a","a","b","b","a","a"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","3","b","2","a","2"].
# Explanation: The groups are "aaa", "bb", and "aa". This compresses to "a3b2a2". Note that each group is independent even if two groups have the same character.
#
#
#  
# Constraints:
#
#
# 	1 <= chars.length <= 2000
# 	chars[i] is a lower-case English letter, upper-case English letter, digit, or symbol.
#
#


#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#
# https://leetcode.com/problems/string-compression/description/
#
# algorithms
# Easy (38.25%)
# Total Accepted:    62.9K
# Total Submissions: 164.5K
# Testcase Example:  '["a","a","b","b","c","c","c"]'
#
# Given an array of characters, compress it in-place.
# 
# The length after compression must always be smaller than or equal to the
# original array.
# 
# Every element of the array should be a character (not int) of length 1.
# 
# After you are done modifying the input array in-place, return the new length
# of the array.
# 
# 
# Follow up:
# Could you solve it using only O(1) extra space?
# 
# 
# Example 1:
# 
# 
# Input:
# ["a","a","b","b","c","c","c"]
# 
# Output:
# Return 6, and the first 6 characters of the input array should be:
# ["a","2","b","2","c","3"]
# 
# Explanation:
# "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by
# "c3".
# 
# 
# 
# 
# Example 2:
# 
# 
# Input:
# ["a"]
# 
# Output:
# Return 1, and the first 1 characters of the input array should be: ["a"]
# 
# Explanation:
# Nothing is replaced.
# 
# 
# 
# 
# Example 3:
# 
# 
# Input:
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# 
# Output:
# Return 4, and the first 4 characters of the input array should be:
# ["a","b","1","2"].
# 
# Explanation:
# Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb"
# is replaced by "b12".
# Notice each digit has it's own entry in the array.
# 
# 
# 
# 
# Note:
# 
# 
# All characters have an ASCII value in [35, 126].
# 1 <= len(chars) <= 1000.
# 
# 
#
class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        result, cnt = 0, 1
        j = 0
        for i in range(1, len(chars)+1): 
            if i < len(chars) and chars[i] == chars[i-1]:
                cnt += 1
            else:
                # 1) update letter
                chars[j] = chars[i-1]
                j += 1
                # 2) update cnt
                if cnt == 1:
                    continue
                for ch in str(cnt):
                    chars[j] = ch
                    j += 1
                # 3) reset cnt
                cnt = 1
        return j
        


