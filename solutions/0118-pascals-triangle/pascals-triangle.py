# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
#
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#
#


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        if numRows == 1:
            return [[1]]
        elif numRows > 1:
            res = self.generate(numRows-1)
            tmp = [1] * numRows
            pre = res[-1]
            for i in range(1,numRows-1):
                tmp[i] = pre[i] + pre[i-1]
            res.append(tmp)
            return res
        
