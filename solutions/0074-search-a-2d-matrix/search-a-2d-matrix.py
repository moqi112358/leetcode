# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
#
# 	Integers in each row are sorted from left to right.
# 	The first integer of each row is greater than the last integer of the previous row.
#
#
#  
# Example 1:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#
#
# Example 2:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#
#
#  
# Constraints:
#
#
# 	m == matrix.length
# 	n == matrix[i].length
# 	1 <= m, n <= 100
# 	-104 <= matrix[i][j], target <= 104
#
#


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        if target < matrix[0][0] and target > matrix[-1][-1]:
            return False
        row_index = self.binarySearch([i[0] for i in matrix], target)
        col_index = self.binarySearch(matrix[row_index], target)
        if matrix[row_index][col_index] == target:
            return True
        else:
            return False
        
    def binarySearch(self, array, target):
        i, j = 0, len(array) - 1
        while i <= j:
            mid = int((i + j) / 2)
            if array[mid] == target:
                return mid
            elif array[mid] < target and (mid == len(array) - 1 or target < array[mid+1]):
                return mid
            elif array[mid] < target:
                i = mid + 1
            elif array[mid] > target:
                j = mid - 1
        return -1
        
        
        
