# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# Example 1:
#
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
#
#
# Example 2:
#
#
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        i, j, m, n = 0, len(matrix[0]) - 1, 0, len(matrix) - 1 
        if len(matrix[0]) == 1:
            return [k[0] for k in matrix]
        res = []
        x, y = 0, 0
        flag = 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        while len(res) < len(matrix[0]) * len(matrix):
            print(x, y, i, j, m, n)
            res.append(matrix[x][y])
            if x == 0 and y == 0:
                flag = 0
                x += dx[flag]
                y += dy[flag]
                continue
            if x == m and y == j and flag == 0:
                m += 1
                flag = 1
            elif x == n and y == j and flag == 1:
                j -= 1
                flag = 2
            elif x == n and y == i and flag == 2:
                n -= 1
                flag = 3
            elif x == m and y == i and flag == 3:
                flag = 0
                i += 1
            x += dx[flag]
            y += dy[flag]
        return res
        
