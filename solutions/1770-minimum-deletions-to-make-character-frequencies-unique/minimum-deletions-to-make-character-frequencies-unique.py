# A string s is called good if there are no two different characters in s that have the same frequency.
#
# Given a string s, return the minimum number of characters you need to delete to make s good.
#
# The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.
#
#  
# Example 1:
#
#
# Input: s = "aab"
# Output: 0
# Explanation: s is already good.
#
#
# Example 2:
#
#
# Input: s = "aaabbbcc"
# Output: 2
# Explanation: You can delete two 'b's resulting in the good string "aaabcc".
# Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
#
# Example 3:
#
#
# Input: s = "ceabaacb"
# Output: 2
# Explanation: You can delete both 'c's resulting in the good string "eabaab".
# Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
#
#
#  
# Constraints:
#
#
# 	1 <= s.length <= 105
# 	s contains only lowercase English letters.
#
#


class Solution:
    def minDeletions(self, s: str) -> int:
        if not s:
            return 0
        count_s = collections.Counter(s)
        count_c_list = list(count_s.values())
        count_c_list.sort()
        res = [0] * (max(count_c_list) + 1)
        delect_count = 0
        for i in count_c_list:
            if res[i] == 0:
                res[i] = 1
            elif res[i] == 1:
                position = i
                while position > 0:
                    if res[position] == 0:
                        break
                    position -= 1
                if position == 0:
                    delect_count += i
                else:
                    res[position] = 1
                    delect_count += (i - position)
        return delect_count
                    
