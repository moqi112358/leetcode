# Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to B, otherwise, return false.
#
# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
#
#  
# Example 1:
#
#
# Input: A = "ab", B = "ba"
# Output: true
# Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.
#
#
# Example 2:
#
#
# Input: A = "ab", B = "ab"
# Output: false
# Explanation: The only letters you can swap are A[0] = 'a' and A[1] = 'b', which results in "ba" != B.
#
#
# Example 3:
#
#
# Input: A = "aa", B = "aa"
# Output: true
# Explanation: You can swap A[0] = 'a' and A[1] = 'a' to get "aa", which is equal to B.
#
#
# Example 4:
#
#
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
#
#
# Example 5:
#
#
# Input: A = "", B = "aa"
# Output: false
#
#
#  
# Constraints:
#
#
# 	0 <= A.length <= 20000
# 	0 <= B.length <= 20000
# 	A and B consist of lowercase letters.
#
#


class Solution:
    # def buddyStrings(self, A: str, B: str) -> bool:
    #     subA, subB, common = '', '', ''
    #     if len(A) != len(B):
    #         return False
    #     for i in range(len(A)):
    #         if len(subA) > 2:
    #             return False
    #         if A[i] == B[i]:
    #             common += A[i]
    #         else:
    #             subA += A[i]
    #             subB += B[i]
    #     if len(subA) != 2 and len(subA) != 0:
    #         return False
    #     elif len(subA) == 2:
    #         if sorted(subA) == sorted(subB):
    #             return True
    #         else:
    #             return False
    #     elif len(subA) == 0:
    #         count = collections.Counter(common)
    #         return any([count[i] > 1 for i in count])
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        
        if A == B and len(set(A)) < len(A):
            return True
        
        diffs = [(a, b) for a, b in zip(A, B) if a!= b]
        
        return len(diffs) == 2 and diffs[0] == diffs[1][::-1]
        
