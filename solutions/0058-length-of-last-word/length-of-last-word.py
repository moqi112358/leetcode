# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a maximal substring consisting of non-space characters only.
#
# Example:
#
#
# Input: "Hello World"
# Output: 5
#
#
#  
#


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        l = s.strip().split(' ')
        return len(l[-1])
        '''
        s = s.strip()
        if len(s) == 0:
            return 0
        l = len(s)
        c = 0
        for i in range(l-1,-1,-1):
            if s[i] != ' ':
                c += 1
            else:
                break
        return c
        
