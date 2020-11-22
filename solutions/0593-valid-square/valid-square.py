# Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.
#
# The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.
#
# A valid square has four equal sides with positive length and four equal angles (90-degree angles).
#
#  
# Example 1:
#
#
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: true
#
#
# Example 2:
#
#
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
# Output: false
#
#
# Example 3:
#
#
# Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
# Output: true
#
#
#  
# Constraints:
#
#
# 	p1.length == p2.length == p3.length == p4.length == 2
# 	-104 <= xi, yi <= 104
#
#


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        #1 chech equal side
        sidelength = []
        for i in range(4):
            for j in range(i+1, 4):
                sidelength.append(self.calside(points[i], points[j]))
        sidelength.sort()
        if not(sidelength[0] == sidelength[1] == sidelength[2] == sidelength[3] and 
               sidelength[4] == sidelength[5] and sidelength[4] > sidelength[0]):
            return False
        if not(2 * sidelength[0] == sidelength[4]):
            return False
        return True
                
                
    def calside(self, p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        
        
