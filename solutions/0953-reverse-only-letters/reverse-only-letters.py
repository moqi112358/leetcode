# -*- coding:utf-8 -*-


# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.
#
#  
#
#
#
#
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: "ab-cd"
# Output: "dc-ba"
#
#
#
# Example 2:
#
#
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
#
#
#
# Example 3:
#
#
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
#
#
#  
#
#
# Note:
#
#
# 	S.length <= 100
# 	33 <= S[i].ASCIIcode <= 122 
# 	S doesn't contain \ or "
#
#
#
#
#


class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        i, j = 0, len(S) - 1
        l = list(S)
        if len(S) == 0:
            return S
        while i < j:
            tmp_i = ord(l[i])
            tmp_j = ord(l[j])
            if tmp_i < 65 or tmp_i > 122 or 90 < tmp_i < 97:
                i += 1
                continue
            if tmp_j < 65 or tmp_j > 122 or 90 < tmp_j < 97:
                j -= 1
                continue
            if 33 <= tmp_i <= 122 and 33 <= tmp_j <= 122:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
        return ''.join(l)
                
