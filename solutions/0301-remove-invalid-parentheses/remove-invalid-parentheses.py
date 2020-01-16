# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
#
# Note: The input string may contain letters other than the parentheses ( and ).
#
# Example 1:
#
#
# Input: "()())()"
# Output: ["()()()", "(())()"]
#
#
# Example 2:
#
#
# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]
#
#
# Example 3:
#
#
# Input: ")("
# Output: [""]
#


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return [""]
        left, right = self.countInvaid(s)
        res = set()
        self.dfs(left, right, 0, 0,  0, 0, res, s)
        return list(res)
        
    
    def valid(self, s):
        left = 0
        for i in s:
            if i == '(':
                left += 1
            elif i == ')':
                left -= 1
            else:
                pass
            if left < 0:
                return False
        if left != 0:
            return False
        return True
    
    def countInvaid(self, s):
        left, right = 0, 0
        for i in s:
            if i == '(':
                left += 1
            elif i == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
            else:
                pass
        return left, right
    
    def dfs(self, total_left, total_right, remove_left, remove_right, left_index, right_index, res, s):
        #print(total_left, total_right,remove_left, remove_right, s)
        if remove_left < total_left:
            for i in range(left_index, len(s)):
                if i > 0 and s[i] == '(' and s[i] == s[i-1]:
                    continue
                if s[i] == '(':
                    self.dfs(total_left, total_right, remove_left+1, remove_right, i, right_index,res, s[:i]+s[i+1:])
        elif remove_right < total_right:
            for i in range(right_index, len(s)):
                if i > 0 and s[i] == ')' and s[i] == s[i-1]:
                    continue
                if s[i] == ')':
                    self.dfs(total_left, total_right, remove_left, remove_right+1, left_index, i, res, s[:i]+s[i+1:])
        elif total_left == remove_left and total_right == remove_right:
            if self.valid(s):
                res.add(s)

        
