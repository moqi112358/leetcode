# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
#
#
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
#
#
# Example:
#
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# return 13.
#
#
#
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ n2.


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return None
        import heapq
        h = []
        heapq.heappush(h, (matrix[0][0], 0, 0))
        while k > 0:
            result, i, j = heapq.heappop(h)
            if i == 0 and j + 1 < len(matrix[0]):
                heapq.heappush(h, (matrix[i][j+1], i, j+1))
            if i + 1 < len(matrix):
                heapq.heappush(h, (matrix[i+1][j], i+1, j))
            k -= 1
        return result
    # search path (num means this value will be searched in #num round)
    # 1 2 3 4
    # 2 3 4
    # 3 4
    # 4
    
