# A web developer needs to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:
#
#
# 	The area of the rectangular web page you designed must equal to the given target area.
# 	The width W should not be larger than the length L, which means L >= W.
# 	The difference between length L and width W should be as small as possible.
#
#
# Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.
#
#  
# Example 1:
#
#
# Input: area = 4
# Output: [2,2]
# Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1]. 
# But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.
#
#
# Example 2:
#
#
# Input: area = 37
# Output: [37,1]
#
#
# Example 3:
#
#
# Input: area = 122122
# Output: [427,286]
#
#
#  
# Constraints:
#
#
# 	1 <= area <= 107
#
#


#
# @lc app=leetcode id=492 lang=python3
#
# [492] Construct the Rectangle
#
# https://leetcode.com/problems/construct-the-rectangle/description/
#
# algorithms
# Easy (48.88%)
# Total Accepted:    47.9K
# Total Submissions: 98.1K
# Testcase Example:  '1'
#
# 
# For a web developer, it is very important to know how to design a web page's
# size. So, given a specific rectangular web page’s area, your job by now is to
# design a rectangular web page, whose length L and width W satisfy the
# following requirements:
# 1. The area of the rectangular web page you designed must equal to the given
# target area.
# 2. The width W should not be larger than the length L, which means L >= W.
# 3. The difference between length L and width W should be as small as
# possible.
# 
# You need to output the length L and the width W of the web page you designed
# in sequence.
# 
# 
# 
# Example:
# 
# Input: 4
# Output: [2, 2]
# Explanation: The target area is 4, and all the possible ways to construct it
# are [1,4], [2,2], [4,1]. 
# But according to requirement 2, [1,4] is illegal; according to requirement
# 3,  [4,1] is not optimal compared to [2,2]. So the length L is 2, and the
# width W is 2.
# 
# 
# 
# Note:
# 
# The given area won't exceed 10,000,000 and is a positive integer
# The web page's width and length you designed must be positive integers.
# 
# 
#
class Solution:
    def constructRectangle(self, area):
        i = 1
        x, y = 1, area
        while i <= area:
            if area % i == 0:
                if i < area / i:
                    x, y = i, area / i
                else:
                    return [int(i), int(area / i)]
            i += 1
        return [int(area), 1]
        


