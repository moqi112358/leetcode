# Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.
#
#  
# Example 1:
#
#
#
#
# Input: hour = 12, minutes = 30
# Output: 165
#
#
# Example 2:
#
#
#
#
# Input: hour = 3, minutes = 30
# Output: 75
#
#
# Example 3:
#
#
#
#
# Input: hour = 3, minutes = 15
# Output: 7.5
#
#
# Example 4:
#
#
# Input: hour = 4, minutes = 50
# Output: 155
#
#
# Example 5:
#
#
# Input: hour = 12, minutes = 0
# Output: 0
#
#
#  
# Constraints:
#
#
# 	1 <= hour <= 12
# 	0 <= minutes <= 59
# 	Answers within 10^-5 of the actual value will be accepted as correct.
#
#


class Solution:
    # def angleClock(self, hour: int, minutes: int) -> float:
    #     minute_degree = minutes / 60 * 360
    #     hour_degree = (hour % 12) / 12 * 360 + minutes / 60 * (360 / 12)
    #     res = abs(minute_degree - hour_degree)
    #     return res if res < 180 else 360 - res
    def angleClock(self, hour: int, minutes: int) -> float:
        return self.method1(hour, minutes)
    
    
    def method1(self, hour, minutes):
        
        per_min = minutes / 60
        per_hr = (hour + per_min) / 12
        
        degree_for_min = per_min * 360
        degree_for_hr = per_hr * 360
        
        res = abs(degree_for_min - degree_for_hr) 
        return res if res <= 180 else 360-res
