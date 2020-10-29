# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note: The solution set must not contain duplicate combinations.
#
#  
# Example 1:
#
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
#
#
#  
# Constraints:
#
#
# 	1 <= candidates.length <= 100
# 	1 <= candidates[i] <= 50
# 	1 <= target <= 30
#
#


class Solution:
    def combinationSum2(self, num, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(num) == 0 or sum(num) < target:
            return []
        res = []
        num = sorted(num)
        self.dfs(num, target, 0, [], res)
        return res
    
    def dfs(self, num, target, start_index, path, res):
        if target == 0:
            res.append(path)
            return
        for i in range(start_index, len(num)):
            if i != start_index and num[i] == num[i-1]:
                continue
            if target < num[i]:
                return
            tmp = self.dfs(num, target - num[i], i + 1, path+[num[i]], res)
        return
