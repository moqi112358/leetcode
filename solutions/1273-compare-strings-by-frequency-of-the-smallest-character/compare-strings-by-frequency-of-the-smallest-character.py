# Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.
#
# Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.
#
#  
# Example 1:
#
#
# Input: queries = ["cbd"], words = ["zaaaz"]
# Output: [1]
# Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
#
#
# Example 2:
#
#
# Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
# Output: [1,2]
# Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").
#
#
#  
# Constraints:
#
#
# 	1 <= queries.length <= 2000
# 	1 <= words.length <= 2000
# 	1 <= queries[i].length, words[i].length <= 10
# 	queries[i][j], words[i][j] are English lowercase letters.
#
#


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        f_q = [self.f(i) for i in queries]
        f_w = [self.f(i) for i in words]
        count_w = [0] * 11
        count_small = [0] * 11
        for i in f_w:
            count_w[i] += 1
        for i in range(9, -1, -1):
            count_small[i] = count_small[i+1] + count_w[i+1]
        return [count_small[i] for i in f_q]
    
    def f(self, string):
        s = sorted(string)[0]
        return string.count(s)
    
    def count_smaller(self, num, l):
        res = 0
        for i in l:
            if i > num:
                res += 1
        return res
