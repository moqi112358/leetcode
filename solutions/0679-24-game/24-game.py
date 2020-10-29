#
# You have 4 cards each containing a number from 1 to 9.  You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.
#
#
# Example 1:
#
# Input: [4, 1, 8, 7]
# Output: True
# Explanation: (8-4) * (7-1) = 24
#
#
#
# Example 2:
#
# Input: [1, 2, 1, 2]
# Output: False
#
#
#
# Note:
#
# The division operator / represents real division, not integer division.  For example, 4 / (1 - 2/3) = 12.
# Every operation done is between two numbers.  In particular, we cannot use - as a unary operator.  For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
# You cannot concatenate numbers together.  For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
#
#
#


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return math.isclose(nums[0], 24)
        res = False
        for item in itertools.combinations(range(len(nums)), 2):
            a, b= item[0], item[1]
            allnum = set(range(len(nums)))
            allnum.remove(a)
            allnum.remove(b)
            for f in [self.add, self.minus, self.production, self.divide, self.redivide]:
                k = f(nums[a], nums[b])
                res = res or self.judgePoint24([nums[i] for i in allnum] + [k])
                if res:
                    return True
        return res
    
    def add(self, a, b):
        return a + b
    
    def minus(self, a, b):
        return abs(a - b)
    
    def production(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b if b != 0 else 0
    
    def redivide(self, a, b):
        return b / a if a != 0 else 0
        
