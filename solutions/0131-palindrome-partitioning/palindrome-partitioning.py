# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# Example:
#
#
# Input: "aab"
# Output:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]
#
#


class Solution:
    def __init__(self):
        self.res = []
        self.l = 0
    def partition(self, s):
        # write your code here
        while self.l < len(s):
            self.helper(s)
        return self.res
    def helper(self, s):
        res = []
        if len(self.res) == 0:
            self.res = [[s[self.l]]]
            self.l += 1
            return
        for i in self.res:
            res.append(i+[s[self.l]])
            if s[self.l] == i[-1][0] and self.check(i[-1][1:]):
                res.append(i[:len(i)-1]+[i[-1]+s[self.l]])
            if len(i) >= 2 and s[self.l] == i[-2] and i[-1] != i[-2]:
                res.append(i[:len(i)-2]+[i[-2]+i[-1]+s[self.l]])
        self.l += 1
        self.res = res
        return
    def check(self,s):
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
