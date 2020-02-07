# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
#
# Example 1:
#
#
# Input: [[1,1],[2,2],[3,3]]
# Output: 3
# Explanation:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4
#
#
# Example 2:
#
#
# Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
# Explanation:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6
#
#
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
#


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        import numpy as np
        if len(points) < 2:
            return len(points)
        res = 1
        for i in range(len(points)):
            slope = {'l': 0}
            same = 0
            for j in range(i+1, len(points)):
                if points[j][0] == points[i][0] and points[j][1] == points[i][1]:
                    same += 1
                    continue
                elif points[j][0] == points[i][0]:
                    slope['l'] += 1
                else:
                    k = (points[j][1] - points[i][1]) * np.longdouble(1) / (points[j][0] - points[i][0])
                    slope[k] = slope.get(k, 0) + 1
            res = max(res, max(slope.values()) + 1 + same)
        return res
