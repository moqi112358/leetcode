# You are playing the following Nim Game with your friend:
#
#
# 	Initially, there is a heap of stones on the table.
# 	You and your friend will alternate taking turns, and you go first.
# 	On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
# 	The one who removes the last stone is the winner.
#
#
# Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.
#
#  
# Example 1:
#
#
# Input: n = 4
# Output: false
# Explanation: These are the possible outcomes:
# 1. You remove 1 stone. Your friend removes 3 stones, including the last stone. Your friend wins.
# 2. You remove 2 stones. Your friend removes 2 stones, including the last stone. Your friend wins.
# 3. You remove 3 stones. Your friend removes the last stone. Your friend wins.
# In all outcomes, your friend wins.
#
#
# Example 2:
#
#
# Input: n = 1
# Output: true
#
#
# Example 3:
#
#
# Input: n = 2
# Output: true
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 231 - 1
#
#


#
# @lc app=leetcode id=292 lang=python3
#
# [292] Nim Game
#
# https://leetcode.com/problems/nim-game/description/
#
# algorithms
# Easy (55.79%)
# Total Accepted:    189.4K
# Total Submissions: 339.4K
# Testcase Example:  '4'
#
# You are playing the following Nim Game with your friend: There is a heap of
# stones on the table, each time one of you take turns to remove 1 to 3 stones.
# The one who removes the last stone will be the winner. You will take the
# first turn to remove the stones.
# 
# Both of you are very clever and have optimal strategies for the game. Write a
# function to determine whether you can win the game given the number of stones
# in the heap.
# 
# Example:
# 
# 
# Input: 4
# Output: false 
# Explanation: If there are 4 stones in the heap, then you will never win the
# game;
# No matter 1, 2, or 3 stones you remove, the last stone will always
# be 
# removed by your friend.
#
class Solution:
    def canWinNim(self, n):
        return n % 4 != 0


