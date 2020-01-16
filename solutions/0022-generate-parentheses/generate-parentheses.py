#
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
#
#
# For example, given n = 3, a solution set is:
#
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
#


class Solution:
	def generateParenthesis(self, n):
		res = []
		self.helper(res, '', n, n, 0)
		return res

	def helper(self, res, s, n, m, left):
		# n - total (
		# m - used (
		if len(s) == 2 * n and left == 0:
			res.append(s)
			return
		if left == 0 and m > 0:
			self.helper(res, s + '(', n, m - 1, left + 1)
		elif left > 0 and m > 0:
			self.helper(res, s + '(', n, m - 1, left + 1)
			self.helper(res, s + ')', n, m, left - 1)
		elif m == 0:
			self.helper(res, s + ')', n, m, left - 1)
		else:
			return

