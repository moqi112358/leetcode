# You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.
#
# Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 
#
# Please note that both secret number and friend's guess may contain duplicate digits.
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
# Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
#
# Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.


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
            
            
        


