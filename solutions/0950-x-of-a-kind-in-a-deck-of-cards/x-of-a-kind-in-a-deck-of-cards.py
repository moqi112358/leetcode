# -*- coding:utf-8 -*-


# In a deck of cards, each card has an integer written on it.
#
# Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:
#
#
# 	Each group has exactly X cards.
# 	All the cards in each group have the same integer.
#
#
#  
#
# Example 1:
#
#
# Input: [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
#
#
#
# Example 2:
#
#
# Input: [1,1,1,2,2,2,3,3]
# Output: false
# Explanation: No possible partition.
#
#
#
# Example 3:
#
#
# Input: [1]
# Output: false
# Explanation: No possible partition.
#
#
#
# Example 4:
#
#
# Input: [1,1]
# Output: true
# Explanation: Possible partition [1,1]
#
#
#
# Example 5:
#
#
# Input: [1,1,2,2,2,2]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[2,2]
#
#
#
#
#
#
#
# Note:
#
#
# 	1 <= deck.length <= 10000
# 	0 <= deck[i] < 10000
#
#
#
#
#
#
#  
#
#
#
#
#


class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        deck_hash = {}
        for i in deck:
            deck_hash[i] = deck_hash.get(i, 0) + 1
        # check X >= 2
        l = list(deck_hash.values())
        check_1 = [i < 2 for i in l]
        if sum(check_1) > 0:
            return False
        min_count = min(l)
        for i in range(2, min_count+1):
            tmp = [c % i != 0 for c in l]
            if sum(tmp) == 0:
                return True
        return False
