# -*- coding:utf-8 -*-


#
# You are standing at position 0 on an infinite number line.  There is a goal at position target.
#
# On each move, you can either go left or right.  During the n-th move (starting from 1), you take n steps.
#
# Return the minimum number of steps required to reach the destination.
#
#
# Example 1:
#
# Input: target = 3
# Output: 2
# Explanation:
# On the first move we step from 0 to 1.
# On the second step we step from 1 to 3.
#
#
#
# Example 2:
#
# Input: target = 2
# Output: 3
# Explanation:
# On the first move we step from 0 to 1.
# On the second move we step  from 1 to -1.
# On the third move we step from -1 to 2.
#
#
#
# Note:
# target will be a non-zero integer in the range [-10^9, 10^9].
#


class Solution(object):
    def reachNumber(self, target):
        t = abs(target)
        n = math.floor(math.sqrt(2*t))
        while True:
            to_minus = ((n+1)*n)/2 - t 
            if to_minus >= 0:  
                if to_minus%2==0:
                    return int(n)
            n+=1
        
