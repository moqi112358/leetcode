# You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).
#
# There is at least one empty seat, and at least one person sitting.
#
# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 
#
# Return that maximum distance to the closest person.
#
#  
# Example 1:
#
#
# Input: seats = [1,0,0,0,1,0,1]
# Output: 2
# Explanation: 
# If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
#
#
# Example 2:
#
#
# Input: seats = [1,0,0,0]
# Output: 3
# Explanation: 
# If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.
#
#
# Example 3:
#
#
# Input: seats = [0,1]
# Output: 1
#
#
#  
# Constraints:
#
#
# 	2 <= seats.length <= 2 * 104
# 	seats[i] is 0 or 1.
# 	At least one seat is empty.
# 	At least one seat is occupied.
#
#


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        seated = [i for i in range(len(seats)) if seats[i] == 1]
        seated_range = [((seated[i] - seated[i-1]) // 2, seated[i], seated[i-1]) for i in range(1, len(seated))]
        if seated[0] != 0:
            seated_range.append((seated[0], seated[0], -1))
        if seated[-1] != len(seats) - 1:
            seated_range.append((len(seats) - 1 - seated[-1], len(seats), seated[-1]))
        max_range = sorted(seated_range, key = lambda x: x[0], reverse = True)[0]
        return max_range[0]
