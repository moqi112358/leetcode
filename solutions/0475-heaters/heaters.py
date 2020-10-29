# Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.
#
# Every house can be warmed, as long as the house is within the heater's warm radius range. 
#
# Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so that those heaters could cover all houses.
#
# Notice that all the heaters follow your radius standard, and the warm radius will the same.
#
#  
# Example 1:
#
#
# Input: houses = [1,2,3], heaters = [2]
# Output: 1
# Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
#
#
# Example 2:
#
#
# Input: houses = [1,2,3,4], heaters = [1,4]
# Output: 1
# Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
#
#
# Example 3:
#
#
# Input: houses = [1,5], heaters = [2]
# Output: 3
#
#
#  
# Constraints:
#
#
# 	1 <= houses.length, heaters.length <= 3 * 104
# 	1 <= houses[i], heaters[i] <= 109
#
#


#
# @lc app=leetcode id=475 lang=python3
#
# [475] Heaters
#
# https://leetcode.com/problems/heaters/description/
#
# algorithms
# Easy (32.21%)
# Total Accepted:    52K
# Total Submissions: 161.3K
# Testcase Example:  '[1,2,3]\n[2]'
#
# Winter is coming! Your first job during the contest is to design a standard
# heater with fixed warm radius to warm all the houses.
# 
# Now, you are given positions of houses and heaters on a horizontal line, find
# out minimum radius of heaters so that all houses could be covered by those
# heaters.
# 
# So, your input will be the positions of houses and heaters seperately, and
# your expected output will be the minimum radius standard of heaters.
# 
# Note:
# 
# 
# Numbers of houses and heaters you are given are non-negative and will not
# exceed 25000.
# Positions of houses and heaters you are given are non-negative and will not
# exceed 10^9.
# As long as a house is in the heaters' warm radius range, it can be
# warmed.
# All the heaters follow your radius standard and the warm radius will the
# same.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3],[2]
# Output: 1
# Explanation: The only heater was placed in the position 2, and if we use the
# radius 1 standard, then all the houses can be warmed.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,4],[1,4]
# Output: 1
# Explanation: The two heater was placed in the position 1 and 4. We need to
# use radius 1 standard, then all the houses can be warmed.
# 
# 
# 
# 
#
class Solution:
    def findRadius(self, houses, heaters):
        # return max([min([abs(j-i) for j in heaters]) for i in houses])
        curr = 0
        houses.sort()
        heaters.sort()
        total_heaters = len(heaters)
        total_houses = len(houses)
        res = -sys.maxsize - 1
        for i in range(total_houses):
            dist1 = abs(heaters[curr] - houses[i])
            while curr != total_heaters - 1 and (abs(heaters[curr + 1] - houses[i]) <= dist1):
                curr += 1
                dist1 = abs(heaters[curr] - houses[i])
            res = max([res, dist1])
        return res

