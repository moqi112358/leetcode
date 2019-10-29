# -*- coding:utf-8 -*-


# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of times.
#
# Note:
#
#
# 	All numbers (including target) will be positive integers.
# 	The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
#
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
#
#


class Solution(object):
    def combinationSum(self, candidates, target):
        # write your code here
        l = sorted(set(candidates))
        res = []
        self.dfs(l, target, [], res)
        return res
        
    def dfs(self, l, target, path, res):
        if target ==  0:
            res.append(path)
            return
        if len(l) == 0 or l[0] > target:
            return
        elif l[0] == target:
            path += [l[0]]
            res.append(path)
            return
        elif l[0] < target:
            for i in range(int(target/l[0])+1):
                self.dfs(l[1:], target - l[0] * i, path + [l[0]] * i, res)
            return
