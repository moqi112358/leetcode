# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
#
#  
#
# Example:
#
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
#
# Output:  [1,2,4,7,5,3,6,8,9]
#
# Explanation:
#
#
#
#  
#
# Note:
#
# The total number of elements of the given matrix will not exceed 10,000.
#


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return None
        nodeSet = collections.defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                indexSum = i + j
                nodeSet[indexSum].append((matrix[i][j], i, j))
        res = []
        for key in range(len(matrix) + len(matrix[0]) - 1):
            nodes = nodeSet[key]
            if key % 2 == 0:
                nodes = sorted(nodes, key = lambda x: x[2])
            else:
                nodes = sorted(nodes, key = lambda x: x[2], reverse = True)
            res.extend([node[0] for node in nodes])
        return res
