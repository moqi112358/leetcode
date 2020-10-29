# You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
#
# Return the number of boomerangs.
#
#  
# Example 1:
#
#
# Input: points = [[0,0],[1,0],[2,0]]
# Output: 2
# Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].
#
#
# Example 2:
#
#
# Input: points = [[1,1],[2,2],[3,3]]
# Output: 2
#
#
# Example 3:
#
#
# Input: points = [[1,1]]
# Output: 0
#
#
#  
# Constraints:
#
#
# 	n == points.length
# 	1 <= n <= 500
# 	points[i].length == 2
# 	-104 <= xi, yi <= 104
# 	All the points are unique.
#
#


#
# @lc app=leetcode id=447 lang=python3
#
# [447] Number of Boomerangs
#
# https://leetcode.com/problems/number-of-boomerangs/description/
#
# algorithms
# Easy (50.38%)
# Total Accepted:    57.9K
# Total Submissions: 114.9K
# Testcase Example:  '[[0,0],[1,0],[2,0]]'
#
# Given n points in the plane that are all pairwise distinct, a "boomerang" is
# a tuple of points (i, j, k) such that the distance between i and j equals the
# distance between i and k (the order of the tuple matters).
# 
# Find the number of boomerangs. You may assume that n will be at most 500 and
# coordinates of points are all in the range [-10000, 10000] (inclusive).
# 
# Example:
# 
# 
# Input:
# [[0,0],[1,0],[2,0]]
# 
# Output:
# 2
# 
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
# 
# 
# 
# 
#
class Solution:
    def numberOfBoomerangs(self, p):
        L, t = len(p), 0
        D = [[0]*L for i in range(L)]
        for i in range(L):
        	E = {}
        	for j in range(L):
        		if j > i: D[i][j] = D[j][i] = (p[j][0]-p[i][0])**2 + (p[j][1]-p[i][1])**2
        		E[D[i][j]] = E[D[i][j]] + 1 if D[i][j] in E else 1
        	t += sum(r*(r-1) for r in E.values())
        return t
		
        
