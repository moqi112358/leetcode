# You are playing the Bulls and Cows game with your friend.
#
# You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:
#
#
# 	The number of "bulls", which are digits in the guess that are in the correct position.
# 	The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
#
#
# Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.
#
# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.
#
#  
# Example 1:
#
#
# Input: secret = "1807", guess = "7810"
# Output: "1A3B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1807"
#   |
# "7810"
#
# Example 2:
#
#
# Input: secret = "1123", guess = "0111"
# Output: "1A1B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1123"        "1123"
#   |      or     |
# "0111"        "0111"
# Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
#
#
# Example 3:
#
#
# Input: secret = "1", guess = "0"
# Output: "0A0B"
#
#
# Example 4:
#
#
# Input: secret = "1", guess = "1"
# Output: "1A0B"
#
#
#  
# Constraints:
#
#
# 	1 <= secret.length, guess.length <= 1000
# 	secret.length == guess.length
# 	secret and guess consist of digits only.
#
#


#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#
# https://leetcode.com/problems/bulls-and-cows/description/
#
# algorithms
# Easy (40.18%)
# Total Accepted:    104.5K
# Total Submissions: 259.9K
# Testcase Example:  '"1807"\n"7810"'
#
# You are playing the following Bulls and Cows game with your friend: You write
# down a number and ask your friend to guess what the number is. Each time your
# friend makes a guess, you provide a hint that indicates how many digits in
# said guess match your secret number exactly in both digit and position
# (called "bulls") and how many digits match the secret number but locate in
# the wrong position (called "cows"). Your friend will use successive guesses
# and hints to eventually derive the secret number.
# 
# Write a function to return a hint according to the secret number and friend's
# guess, use A to indicate the bulls and B to indicate the cows. 
# 
# Please note that both secret number and friend's guess may contain duplicate
# digits.
# 
# Example 1:
# 
# 
# Input: secret = "1807", guess = "7810"
# 
# Output: "1A3B"
# 
# Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
# 
# Example 2:
# 
# 
# Input: secret = "1123", guess = "0111"
# 
# Output: "1A1B"
# 
# Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a
# cow.
# 
# Note: You may assume that the secret number and your friend's guess only
# contain digits, and their lengths are always equal.
#
class Solution:
    def getHint(self, secret, guess) -> str:
        A, B = 0, 0
        secret_hash = {}
        guess_hash = {}
        A_hash = {}
        for i in range(len(secret)):
            secret_hash[secret[i]] =  secret_hash.get(secret[i], 0) + 1
            guess_hash[guess[i]] =  guess_hash.get(guess[i], 0) + 1
            if secret[i] == guess[i]:
                A += 1
                A_hash[secret[i]] = A_hash.get(secret[i], 0) + 1
        for i in secret_hash:
            B += (min(secret_hash[i], guess_hash.get(i, 0))) - A_hash.get(i, 0)
        return str(A) + 'A' + str(B) + 'B'
            
            
        


