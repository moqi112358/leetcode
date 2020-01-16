# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
#
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
#
# Example 1:
#
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
#
#
# Example 2:
#
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
#


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        for i in range(len(s)):
            if i != 0:
                if s[i] != '0':
                    dp[i+1] += dp[i]
                tmp = int(s[i-1:i+1])
                if 10 <= tmp <= 26:
                    dp[i+1] = dp[i+1] + dp[i-1] if i != 1 else dp[i+1] + 1
                if dp[i+1] == 0:
                    return 0
            elif i == 0:
                tmp = int(s[i])
                if tmp == 0:
                    return 0
                else:
                    dp[i+1] = 1
        print(dp)
        return dp[-1]
        
