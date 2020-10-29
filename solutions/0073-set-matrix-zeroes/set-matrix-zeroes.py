# Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.
#
# Follow up:
#
#
# 	A straight forward solution using O(mn) space is probably a bad idea.
# 	A simple improvement uses O(m + n) space, but still not the best solution.
# 	Could you devise a constant space solution?
#
#
#  
# Example 1:
#
#
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
#
#
# Example 2:
#
#
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#
#
#  
# Constraints:
#
#
# 	m == matrix.length
# 	n == matrix[0].length
# 	1 <= m, n <= 200
# 	-231 <= matrix[i][j] <= 231 - 1
#
#


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        is_row, is_col = False, False
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    if j == 0:
                        is_col = True
                    if i == 0:
                        is_row = True
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if is_col:
            for i in range(row):
                matrix[i][0] = 0
        if is_row:
            for j in range(col):
                matrix[0][j] = 0
        return matrix
