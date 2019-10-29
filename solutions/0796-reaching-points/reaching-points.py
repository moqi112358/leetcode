# -*- coding:utf-8 -*-


# A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).
#
# Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.
#
#
# Examples:
# Input: sx = 1, sy = 1, tx = 3, ty = 5
# Output: True
# Explanation:
# One series of moves that transforms the starting point to the target is:
# (1, 1) -> (1, 2)
# (1, 2) -> (3, 2)
# (3, 2) -> (3, 5)
#
# Input: sx = 1, sy = 1, tx = 2, ty = 2
# Output: False
#
# Input: sx = 1, sy = 1, tx = 1, ty = 1
# Output: True
#
#
#
# Note:
#
#
# 	sx, sy, tx, ty will all be integers in the range [1, 10^9].
#
#


class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        '''
        queue = [(sx,sy)]
        count = 0
        while queue:
            (x, y) = queue.pop(0)
            if x == tx and y == ty:
                count += 1
                continue
            if x > tx or y > ty:
                continue
            if x + y <= ty:
                queue.append((x,x+y))
            if x + y <= tx:
                queue.append((x+y,y))
        return count == 1
        '''
        while sx<tx and sy<ty: tx,ty = tx%ty,ty%tx
        return sx==tx and (ty-sy)%sx==0 or sy==ty and (tx-sx)%sy==0
        
