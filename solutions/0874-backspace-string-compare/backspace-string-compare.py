# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
#
# Note that after backspacing an empty text, the text will continue empty.
#
#
# Example 1:
#
#
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
#
#
#
# Example 2:
#
#
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
#
#
#
# Example 3:
#
#
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
#
#
#
# Example 4:
#
#
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
#
#
# Note:
#
#
# 	1 <= S.length <= 200
# 	1 <= T.length <= 200
# 	S and T only contain lowercase letters and '#' characters.
#
#
# Follow up:
#
#
# 	Can you solve it in O(N) time and O(1) space?
#
#
#
#
#
#


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        new_s, new_t = '', ''
        count_s, count_t = 0, 0
        for i in range(len(S)-1, -1, -1):
            if S[i] == '#':
                count_s += 1
            if S[i] != '#':
                if count_s == 0:
                    new_s += S[i]
                else:
                    count_s -= 1
        for i in range(len(T)-1, -1, -1):
            if T[i] == '#':
                count_t += 1
            if T[i] != '#':
                if count_t == 0:
                    new_t += T[i]
                else:
                    count_t -= 1
        return new_s == new_t
