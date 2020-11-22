# There is a special square room with mirrors on each of the four walls.  Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.
#
# The square room has walls of length p, and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.
#
# Return the number of the receptor that the ray meets first.  (It is guaranteed that the ray will meet a receptor eventually.)
#
#  
#
#
# Example 1:
#
#
# Input: p = 2, q = 1
# Output: 2
# Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.
#
#
#
# Note:
#
#
# 	1 <= p <= 1000
# 	0 <= q <= p
#
#
#


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        destination = { (p, 0): 0, (p, p): 1, (0, p): 2}
        point1, point2 = (0, 0), (p, q)
        while True:
            for point in destination:
                if abs(point[0] - point2[0]) < 0.0001 and abs(point[1] - point2[1]) < 0.0001:
                    return destination[point]
            point1, point2 = self.calNextpoint(point1, point2, p, q)
        return
    
    def calNextpoint(self, point1, point2, p, q):
        # line1 y = 0
        # line2 y = p
        # line3 x = 0
        # line4 x = p
        if point2[0] == 0 or point2[0] == p:
            # 上下对称
            re_point1 = (point1[0], point1[1] + 2 * (point2[1] - point1[1]))
        elif point2[1] == 0 or point2[1] == p:
            # 左右对称
            re_point1 = (point1[0] + 2 * (point2[0] - point1[0]), point1[1])
        newline_k = (re_point1[1] - point2[1]) / (re_point1[0] - point2[0])
        newline_b = point2[1] - newline_k * point2[0]
        line1_point = (-1 * newline_b / newline_k , 0)
        line2_point = ((p - newline_b) / newline_k, p)
        line3_point = (0, newline_b)
        line4_point = (p, p * newline_k + newline_b)
        for point in [line1_point, line2_point, line3_point, line4_point]:
            if  not(abs(point[0] - point2[0]) < 0.0001 and abs(point[1] - point2[1]) < 0.0001) and 0 <= point[0] <= p and 0 <= point[1] <= p:
                res_point = point
        return point2, res_point
