# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
#
# Note:
#
#
# 	Given target value is a floating point.
# 	You are guaranteed to have only one unique value in the BST that is closest to the target.
#
#
# Example:
#
#
# Input: root = [4,2,5,1,3], target = 3.714286
#
#     4
#    / \
#   2   5
#  / \
# 1   3
#
# Output: 4
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        diff = float('inf')
        res = None
        cur = root
        while cur:
            cur_diff = abs(target - cur.val)
            if cur_diff <= diff:
                diff, res = cur_diff, cur.val
            if target >= cur.val:
                cur = cur.right
            else:
                cur = cur.left
        return res
        
